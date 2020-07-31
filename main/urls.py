from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.drag, name='drag'),
    path('index', views.index, name='index'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]  + static(settings.MEDIA_URL, media_root=settings.MEDIA_ROOT)


