from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.SignupView.as_view(), name='signup'),
    path('signout', views.signout_view, name='signout'),
    path('signin', views.SigninView.as_view(), name='signin'),
    path('profile', views.ProifleView.as_view(), name='profile')
]
