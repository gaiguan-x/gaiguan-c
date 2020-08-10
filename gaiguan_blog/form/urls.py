# coding:utf-8
from django.urls import path
from .views import register, add_info, get_all_forms, display_all_forms, search_form

urlpatterns = [
    path('regist/<str:keyword>', register, name='regist'),
    path('info/', add_info, name='info'),
    path('forms/', display_all_forms, name='forms'),
    path('get_forms/', get_all_forms, name='get_forms'),
    path('search_form/', search_form, name='search_form'),
    # path('get_cities/', get_cities, name='get_cities'),
    # path('get_districts/', get_districts, name='get_districts'),
]
