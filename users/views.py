from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView

from . import forms


class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class SignupView(CreateView):
    form_class = forms.SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url, permanent=True)


class SigninView(LoginView):
    form_class = forms.SigninForm
    template_name = 'users/signin.html'

    def get_success_url(self) -> str:
        return reverse_lazy('index')


def signout_view(request):
    logout(request)
    return redirect('signin', permanent=True)
