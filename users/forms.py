from itertools import chain

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from . import utils


class SignupForm(utils.AddClassMixin, UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.add_classes('form-control')

  class Meta(UserCreationForm.Meta):
    fields = ['username', 'email', 'password1', 'password2']


class SigninForm(utils.AddClassMixin, AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.add_classes('form-control')

  class Meta:
    fields = ['username', 'password']
