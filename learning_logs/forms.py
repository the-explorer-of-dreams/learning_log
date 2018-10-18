#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     forms
   Description :
   Author :       william
   date：          2018/10/18
-------------------------------------------------
   Change Activity:
                   2018/10/18:
-------------------------------------------------
"""
__author__ = 'william'

from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """创建Topic的表单"""

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """创建Topic的表单"""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}
