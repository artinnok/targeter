from django.contrib import admin
from django.contrib.auth import models


# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
