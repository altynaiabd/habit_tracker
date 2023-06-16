from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
        ('o', 'Другое'),
    )
    first_name = models.CharField(verbose_name='Имя', max_length=50, default='')
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDER, default='')
    birth_date = models.DateField(verbose_name='Дата рождения', default='2000-09-12')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'