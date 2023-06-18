from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    GENDER = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
        ('o', 'Другое'),
    )
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER, default='')
    birth_date = models.DateField(verbose_name='Дата рождения', default='2000-09-12')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
