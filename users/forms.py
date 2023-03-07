from itertools import chain

from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({'class': 'form-control'})

  class Meta(UserCreationForm.Meta):
    fields = ['username', 'email', 'password1', 'password2']
