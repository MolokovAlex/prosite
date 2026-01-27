"""
URL configuration for prosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from sklad_pro.views import index
from sklad_pro.views import edit_DBG


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', index, name='first_page'),
    # path ('edit_DBG/', edit_DBG, name='edit_DBG'),
    path("edit_DBG/", edit_DBG, name='edit_DBG'),
]
