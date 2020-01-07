"""Romanian_Alpine_Club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from home import urls as urls_home
from blog import urls as urls_blog
from users import views as user_views
from products import urls as urls_products
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(urls_home)),
    url(r"^register/", user_views.register, name="register"),
    url(r"^profile/", user_views.profile, name="profile"),
    url(
        r"^login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    url(
        r"^logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    url(
        r"^password-reset/$",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset.html"
        ),
        name="password_reset",
    ),
    url(
        r"^password-reset/done/$",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    url(
        r"^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+) - (?P<token>.+)/$",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    url(
        r"^password-reset-complete/$",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    url(r"^blog/", include(urls_blog)),
    url(r"^products/", include(urls_products)),
    url(r"^media/(?P<path>.*)$", static.serve, {"document_root": MEDIA_ROOT}),
]

# """To run in development and DEBUG mode is True"""

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
