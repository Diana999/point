from django.urls import path
from . import views
urlpatterns = [
    path('', views.dream_list, name='dream_list'),
]