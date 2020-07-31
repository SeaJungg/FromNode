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
    path('upload_node/', views.upload_node, name='upload_node'),
    # path('upload_list/', views.upload_list, name='upload_list'),
    path('upload_list/', views.NodeListView.as_view(), name = 'upload_list'),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


