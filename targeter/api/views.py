from datetime import datetime

import requests
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect

from core.models import User, Post, Coordinate
from api.fetch import fetch_media
from api.filter import is_old, has_caption
from api.serializers import PostSerializer


class AuthorizeView(APIView):
    """
    Авторизует пользователя в приложении
    """
    url = ('https://api.instagram.com/oauth/authorize/?'
           'client_id={client_id}&'
           'redirect_uri={redirect_uri}&'
           'response_type=code&'
           'scope={scope}')

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI,
            scope='public_content follower_list comments relationships likes'
        ))


class CallbackView(APIView):
    """
    Сюда придет коллбэк от Инстаграма
    """
    url = 'https://api.instagram.com/oauth/access_token'

    def get(self, request, *args, **kwargs):
        code = request.query_params['code']

        # send auth data to Instagram servers
        json = requests.post(self.url, data={
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'redirect_uri': settings.REDIRECT_URI,
            'code': code,
            'grant_type': 'authorization_code',
        }).json()

        # save retrieved data
        User.objects.update_or_create(
            user_id=json['user']['id'],
            defaults={
                'username': json['user']['username'],
                'access_token': json['access_token']
            })
        return Response(json['user'])


class StartView(APIView):
    """
    Сохраняет данные по локациям
    """
    def get(self, request, *args, **kwargs):
        for coordinate in Coordinate.objects.exclude(user__access_token=None):
            res = fetch_media.delay(
                coordinate.user.access_token,
                coordinate.lat,
                coordinate.lng
            ).get()

            # filter useless data
            data = filter(is_old, res['data'])
            data = filter(has_caption, data)

            # save good data
            for post in data:
                user, created = User.objects.update_or_create(
                    user_id=post['user']['id'],
                    defaults={'username': post['user']['username']}
                )

                created_time = datetime.fromtimestamp(int(post['created_time']))
                Post.objects.update_or_create(
                    post_id=post['id'],
                    defaults={
                        'text': post['caption']['text'],
                        'created_time': created_time,
                        'user': user
                    }
                )
        return Response(data)


class GoodView(ListAPIView):
    """
    Получает данные
    """
    serializer_class = PostSerializer
    queryset = Post.objects.filter(text__icontains='продаю')
