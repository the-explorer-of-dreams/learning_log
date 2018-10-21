#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""定义users的url模式"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    #login
    path('login/', LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', views.logout_view, name='logout'),
    path(r'register/', views.register, name='register'),

]
