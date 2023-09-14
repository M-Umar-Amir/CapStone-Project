from django.contrib import admin
from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth-token/', obtain_auth_token),
    path('app/', index, name='index'),
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='single_menu'),
]
