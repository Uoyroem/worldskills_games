from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout, login, authenticate

from . import forms


class SignupView(CreateView):
  form_class = forms.SignupForm
  template_name = 'users/signup.html'
  success_url = reverse_lazy('index')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect(self.get_success_url(), permanent=True)


def logout_view(request):
  logout(request)
  return redirect('index', permanent=True)
