from django.urls import path
from .views import create_view,list_view ,detail_view
urlpatterns = [
    path('home/',create_view, name="home"),
    path('list/',list_view, name="list-views"),
    path('<int:id>',detail_view, name='detail_view'),
]
