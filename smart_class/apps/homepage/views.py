__all__ = ()

import django.views.generic


class Home(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/main.html")


class Games(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/games.html")
