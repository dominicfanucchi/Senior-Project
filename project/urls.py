from django.urls import path
from . import views


app_name = 'senior project'
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('speech/', views.speech, name='speech'),
    path('nlp', views.nlp, name='nlp'),
]