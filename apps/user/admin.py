from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.user.models import UserModel


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    model = UserModel
    list_display = ['username', 'first_name', 'gender', 'birth_date']

