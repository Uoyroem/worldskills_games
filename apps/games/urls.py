from django.urls import path, include
from . import views

app_name = 'games'

detail_urlpatterns = [
    path('delete', views.GameDeleteView.as_view(), name='delete'),
    path('manage', views.ManageGameView.as_view(), name='manage'),
    path('', views.GameView.as_view(), name='detail')
]

urlpatterns = [
    path('<slug:slug>/', include(detail_urlpatterns)),
    path('new', views.GameCreateView.as_view(), name='new'),
    path('', views.GameListView.as_view(), name='list')
]
