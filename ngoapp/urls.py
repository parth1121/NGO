from django.urls import path

from ngoapp import views

urlpatterns = [
    path('', views.index),
]