from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from . import views

from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/', views.Blog, name='blog'),
    path('tools/', views.Tools, name='tools'),
    path('<slug:slug>', views.single_post, name='single_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)