from django.urls import path
from .views import create_view,list_view ,detail_view,update,delete
urlpatterns = [
    path('home/',create_view, name="home"),
    path('delete/<int:id>/',delete, name="delete"),
    path('update/<int:id>/',update, name="update"),
    path('list/',list_view, name="list-views"),
    path('<int:id>',detail_view, name='detail_view'),
]
