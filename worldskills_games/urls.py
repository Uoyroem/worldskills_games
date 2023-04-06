from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework import routers

from apps.games import views

router = routers.SimpleRouter()
router.register('games', views.GameViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('', include('apps.games.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
