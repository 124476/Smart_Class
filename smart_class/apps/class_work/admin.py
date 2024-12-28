__all__ = ()

import django.contrib.admin

import apps.class_work.models


@django.contrib.admin.register(apps.class_work.models.Work)
class WorkAdmin(django.contrib.admin.ModelAdmin):
    pass


@django.contrib.admin.register(apps.class_work.models.Computer)
class ComputerAdmin(django.contrib.admin.ModelAdmin):
    pass
