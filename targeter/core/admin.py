from django.contrib import admin
from django.contrib.auth import models

from core.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'access_token')

admin.site.register(User, UserAdmin)


# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
