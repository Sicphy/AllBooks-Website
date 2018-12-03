from django.contrib import admin
from django.urls import path
from accounts.views import ProfilePageView, PasswordPageView, DeleteAccountPageView
import re
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^profile/$', login_required(ProfilePageView.as_view()), name = "change_profile"),
    url(r'^password/$', login_required(PasswordPageView.as_view()), name = "change_password"),
    url(r'^delete/$', login_required(DeleteAccountPageView.as_view()), name = "delete_account"),
]
