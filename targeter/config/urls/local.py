import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *


urlpatterns = urlpatterns + [
    url(
        regex=r'^__debug__/',
        view=include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
