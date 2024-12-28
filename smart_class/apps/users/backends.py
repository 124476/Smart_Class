__all__ = ()
import django.conf
import django.contrib.auth.backends
import django.urls
import django.utils.timezone

import apps.users.models


class AuthenticateBackend(django.contrib.auth.backends.ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if "@" in username:
                user = apps.users.models.User.objects.by_mail(
                    email=username,
                )
            else:
                user = apps.users.models.User.objects.get(username=username)
        except apps.users.models.User.DoesNotExist:
            return None

        if user.check_password(password):
            user.attempts_count = 0
            user.save()
            return user

        user.attempts_count += 1
        if user.attempts_count >= django.conf.settings.MAX_AUTH_ATTEMPTS:
            user.blocked_time = django.utils.timezone.now()
            user.is_active = False
            user.save()

            mail_url = django.urls.reverse(
                "users:unblock",
                args=[user.username],
            )
            url = f"{request.scheme}://{request.get_host()}{mail_url}"
            django.core.mail.send_mail(
                subject=user.username,
                message="У вас неделя на восстановление "
                "профиля на нашем сайте\n"
                f"вот ссылка: {url}",
                from_email=django.conf.settings.DEFAULT_FROM_EMAIL,
                recipient_list=[
                    user.email,
                ],
                fail_silently=False,
            )

        user.save()

        return None
