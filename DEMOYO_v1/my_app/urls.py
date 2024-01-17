from django.contrib import admin
from django.urls import path
from .views import logine, main, register,logouts
urlpatterns = [
    path('register/', register, name='register' ),
    path('login/', logine, name="logine"),
    path('logouts/', logouts, name="logouts")
]