from django.contrib import admin
from django.urls import path
from accounts.views import ProfilePageView,PasswordPageView
import re
from django.conf.urls import url

urlpatterns = [
    url(r'^profile/$', ProfilePageView.as_view(), name = "change_profile"),
    url(r'^password/$', PasswordPageView.as_view(), name = "change_password"),
]
