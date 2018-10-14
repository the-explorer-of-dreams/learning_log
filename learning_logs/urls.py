#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    # index
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),


]
