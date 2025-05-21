from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_post, name='generate_post'),
]