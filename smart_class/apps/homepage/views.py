__all__ = ()

import django.views.generic


class Home(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/main.html")

class Games(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/games.html")

class Tatarlango(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/tatarlango.html")

class EntangledTale(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "homepage/entangled_tale.html")