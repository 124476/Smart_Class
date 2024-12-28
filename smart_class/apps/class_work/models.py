__all__ = ()

import django.contrib.auth
import django.db.models

import uuid


class Work(django.db.models.Model):
    user = django.db.models.ForeignKey(
        django.contrib.auth.get_user_model(),
        on_delete=django.db.models.CASCADE,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "класс"
        verbose_name_plural = "классы"

    def __str__(self):
        return f"{self.name} ({self.user})"


class Computer(django.db.models.Model):
    uuid = django.db.models.UUIDField(
        verbose_name="уникальный идентификатор",
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    name = django.db.models.CharField(
        verbose_name="название",
        max_length=150,
        null=False,
        unique=False,
    )
    work = django.db.models.ForeignKey(
        Work,
        verbose_name="класс",
        null=True,
        on_delete=django.db.models.CASCADE,
    )
    is_active = django.db.models.BooleanField(
        verbose_name="включен",
        default=True,
    )
    signal = django.db.models.BooleanField(
        verbose_name="сигнал",
        default=False,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "компьютер"
        verbose_name_plural = "компьютеры"

    def __str__(self):
        return f"{self.name} ({self.work.name}) - {self.uuid}"
