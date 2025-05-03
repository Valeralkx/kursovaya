from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_('Аватар'))
    bio = models.TextField(max_length=500, blank=True, verbose_name=_('О себе'))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_('Телефон'))
    
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return self.username