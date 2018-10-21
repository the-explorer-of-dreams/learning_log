#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    # index
    path(r'', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    path(r'topic/<int:topic_id>/', views.topic, name='topic'),
    path(r'new_topic/', views.new_topic, name='new_topic'),
    path(r'new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path(r'edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


]
