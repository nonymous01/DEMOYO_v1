from django.contrib import admin
from django.urls import path
from .views import logine, main, register
urlpatterns = [
    path('register/', register, name='register' ),
    path('login/', logine, name="logine")
]