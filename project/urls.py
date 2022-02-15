from django.urls import path
from . import views


app_name = 'senior project'
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
]