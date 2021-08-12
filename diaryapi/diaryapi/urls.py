"""diaryapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path, include
from rest_framework import routers

from diary.views import DiaryListCreateView,UserView, DiaryGetDestroyUpdateView


#create a router for the api
router = routers.DefaultRouter()

#register the views with the router

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/', include(router.urls)),
    path('api/account/', UserView.as_view(),name='account'),
    path('api/diarys/<str:key>/',DiaryListCreateView.as_view(), name='diary-list'),
    
    re_path(r'^api/diarys/(?P<key>\w*)/(?P<id>\d+)$',DiaryGetDestroyUpdateView.as_view(), name='diary-detail'),


]
