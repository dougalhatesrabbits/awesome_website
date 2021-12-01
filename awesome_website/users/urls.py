from django.conf.urls import include, url
from .views import dashboard, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^oauth/", include("social_django.urls", namespace='social')),
    url(r"^register/", register, name="register"),
]
