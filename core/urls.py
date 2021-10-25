from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('booklist/',BookListFilter.as_view(),name="BookListFilterFilter"),
    path('bookcreate/',BookCreate.as_view(),name="BookListFilterFilter")
]
