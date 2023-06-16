from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.user.models import UserModel


class UserModelCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'gender', 'birth_date')


class UserModelChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'gender', 'birth_date')