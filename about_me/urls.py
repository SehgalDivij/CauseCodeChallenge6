from django.conf.urls import url, include
from django.contrib import admin
from .views import Profiles

urlpatterns = [
    url(r'^', Profiles.as_view(), name="Profiles"),
]
