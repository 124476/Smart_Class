__all__ = ()

import django.contrib.auth.models
from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import delete, get_thumbnail


class Manager(django.contrib.auth.models.UserManager):
    def by_mail(self, email):
        return self.get(
            **{self.model.EMAIL_FIELD: self.normalize_email(email)},
        )


class User(AbstractUser):
    objects = Manager()
    avatar = models.ImageField(
        _("avatar"),
        upload_to="avatars/",
        null=True,
        blank=True,
    )
    attempts_count = models.IntegerField(default=0)
    blocked_time = models.DateTimeField(
        default=django.utils.timezone.now,
    )

    def has_avatar(self):
        return self.avatar and self.avatar.url is not None

    def get_small_avatar(self):
        return get_thumbnail(self.avatar, "80", crop="center").url

    def get_large_avatar(self):
        return get_thumbnail(self.avatar, "200", crop="center").url

    def save(self, *args, **kwargs):
        try:
            old = User.objects.get(pk=self.pk)
            if old.has_avatar() and not self.has_avatar():
                delete(old.avatar)
        except User.DoesNotExist:
            pass

        super().save(*args, **kwargs)
