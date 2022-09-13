from django.urls import path, include
from pgenerator import views

urlpatterns = [
    path('', views.home, name='pgen-home'),
]
