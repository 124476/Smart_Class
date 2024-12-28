__all__ = ()

import django.conf
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
import django.utils
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.edit import FormView

from apps.users.forms import UserForm
from apps.users.models import User


class AccountView(LoginRequiredMixin, FormView):
    template_name = "users/profile.html"
    form_class = UserForm

    def get_initial(self):
        return {
            "username": self.request.user.username,
            "email": self.request.user.email,
            "avatar": self.request.user.avatar,
        }

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post["email"] = request.user.email
        user_form = UserForm(post, request.FILES, instance=request.user)
        new_username = user_form.cleaned_data.get("username")

        if new_username != request.user.username:
            if user_form.is_valid():
                if User.objects.filter(username=new_username).exists():
                    user_form.add_error(
                        "username",
                        _("username_is_already_taken"),
                    )
        elif user_form.is_valid():
            user_form.save()
            return redirect("users:profile")

        return render(request, "users/profile.html", {"form": user_form})


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    pass


class UnblockView(View):
    def get(self, *args, **kwargs):
        obj = get_object_or_404(
            User.objects,
            username=kwargs.get("username"),
        )
        date = obj.blocked_time
        hours = django.utils.timezone.now() - date
        hours = hours.total_seconds() / 3600
        if obj.attempts_count >= django.conf.settings.MAX_AUTH_ATTEMPTS:
            if hours < 24 * 7:
                obj.is_active = True
                obj.save()

        return redirect("users:login")
