"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#re_path(r'^admin/', admin.site.urls),
urlpatterns = [
    re_path(r'^login/$', auth_views.login, {'template_name': 'master/login.html'}, name='login'),
    re_path(r'^master/', include('master.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('home.urls')),
    re_path(r'^projects/', include('projects.urls', namespace="create_post")),
    re_path(r'^contact/', include('contact.urls')),
]

# To make images work
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
