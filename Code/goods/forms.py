from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from goods.models import Good

class GoodForm(forms.ModelForm):
  class Meta:
    model = Good
    fields = '__all__'


class RegisterFormView(FormView):
  form_class = UserCreationForm
  success_url = "/login/"
  template_name = "register.html"

  def form_valid(self, form):
    form.save()
    return super(RegisterFormView, self).form_valid(form)
