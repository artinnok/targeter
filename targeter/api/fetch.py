import requests
from celery import shared_task


def base_fetch(method, access_token, parameters=''):
    url = ('https://api.instagram.com/v1'
           '{method_name}?'
           'access_token={access_token}&'
           '{parameters}')
    return requests.get(url.format(
        method_name=method,
        access_token=access_token,
        parameters=parameters
    )).json()


@shared_task(name='fetch', rate_limit='500/h')
def fetch(*args):
    return base_fetch(*args)
