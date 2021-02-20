from django.contrib import admin
from django.urls import path,include
from googlelogin import views

urlpatterns = [
    path('',views.index)
]
