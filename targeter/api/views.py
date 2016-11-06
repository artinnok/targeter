import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect


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
            scope='public_content likes'
        ))


class CallbackView(APIView):
    """
    Сюда придет коллбэк от Инстаграма
    """
    url = 'https://api.instagram.com/oauth/access_token'

    def get(self, request, *args, **kwargs):
        code = request.query_params['code']
        json = requests.post(self.url, data={
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'redirect_uri': settings.REDIRECT_URI,
            'code': code,
            'grant_type': 'authorization_code',
        }).json()
        return Response(json)

