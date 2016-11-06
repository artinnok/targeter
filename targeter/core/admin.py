from django.contrib import admin
from django.contrib.auth import models

from core.models import User, KeyWord


class KeyWordInline(admin.StackedInline):
    model = KeyWord
    extra = 1
    fields = ('name',)


class UserAdmin(admin.ModelAdmin):
    inlines = [KeyWordInline]
    list_display = ('user_id', 'username', 'access_token')

admin.site.register(User, UserAdmin)


# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
