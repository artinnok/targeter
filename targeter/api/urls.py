from django.conf.urls import url

from api.views import AuthorizeView, CallbackView, StartView, GoodView


urlpatterns = [
    url(
        regex=r'^authorize/$',
        view=AuthorizeView.as_view(),
        name='authorize'
    ),
    url(
        regex=r'^callback/$',
        view=CallbackView.as_view(),
        name='callback'
    ),
    url(
        regex=r'^start/$',
        view=StartView.as_view(),
        name='start'
    ),
    url(regex=r'^good/$',
        view=GoodView.as_view(),
        name='good'
    ),
]
