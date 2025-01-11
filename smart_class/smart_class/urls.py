__all__ = ()
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.users.urls")),
    path("auth/", include("allauth.urls")),
    path(
        "",
        include("apps.homepage.urls"),
    ),
    path(
        "class_work/",
        include("apps.class_work.urls"),
    ),
    path(
        "api/",
        include("apps.api.urls"),
    ),
    path(
        "ckeditor/",
        include("ckeditor_uploader.urls"),
    ),
    path("i18n/", include("django.conf.urls.i18n")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
