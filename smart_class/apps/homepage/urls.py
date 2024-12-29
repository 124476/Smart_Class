from django.urls import path

import apps.homepage.views

app_name = "homepage"
urlpatterns = [
    path("", apps.homepage.views.Home.as_view(), name="main"),
    path("games/", apps.homepage.views.Games.as_view(), name="games"),
    path("tatarlango/", apps.homepage.views.Tatarlango.as_view(), name="tatarlango"),
    path("entangled_tale/", apps.homepage.views.EntangledTale.as_view(), name="entangled_tale"),
]
