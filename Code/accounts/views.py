from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from django.contrib.auth.models import User

from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from goods.models import Good
from genres.models import Genre

class ProfilePageView(TemplateView, CategoryListMixin):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        self.user_form = UserForm(instance=request.user)
        return super(ProfilePageView, self).get(request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        context["user_form"] = self.user_form
        return context

    def post(self, request, *args, **kwargs):
        self.user_form = UserForm(request.POST, instance=request.user)
        if self.user_form.is_valid():
            self.user_form.save()
            messages.add_message(request, messages.SUCCESS, "Ваш профиль был успешно обновлён !")
            return redirect('main')
        else:
            messages.add_message(request, messages.ERROR, "Please correct the error below.")
        return super(ProfilePageView, self).get(request, *args, **kwargs)

class PasswordPageView(TemplateView, CategoryListMixin):
    template_name = "change_password.html"
    
    def get(self, request, *args, **kwargs):
        self.form = PasswordChangeForm(request.user)
        return super(PasswordPageView, self).get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(PasswordPageView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = PasswordChangeForm(request.user, request.POST)
        if self.form.is_valid():
            user = self.form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request, messages.SUCCESS, "Ваш пароль был успешно обновлён !")
            return redirect('main')
        else:
            messages.add_message(request, messages.ERROR, "Please correct the error below.")
        return super(PasswordPageView, self).get(request, *args, **kwargs)


class DeleteAccountPageView(TemplateView, CategoryListMixin):
    template_name = "delete_account.html"
    
    def get(self, request, *args, **kwargs):
        return super(DeleteAccountPageView, self).get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(DeleteAccountPageView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        request.user.is_active = False
        request.user.save()
        return redirect('main')
