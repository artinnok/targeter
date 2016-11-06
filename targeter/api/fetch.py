import requests
from celery import shared_task


def base_fetch(method, access_token, parameters=''):
    url = ('https://api.instagram.com/v1'
           '{method}?'
           'access_token={access_token}&'
           '{parameters}')
    return requests.get(url.format(
        method=method,
        access_token=access_token,
        parameters=parameters
    )).json()


@shared_task(name='fetch', rate_limit='500/h')
def fetch(*args):
    return base_fetch(*args)


@shared_task(name='fetch_media', rate_limit='500/h')
def fetch_media(access_token, lat, lng):
    method = '/media/search/'
    parameters = ('lat={lat}&'
                  'lng={lng}&'
                  'distance=5000'.format(lat=lat,
                                         lng=lng))

    return base_fetch(method, access_token, parameters)
