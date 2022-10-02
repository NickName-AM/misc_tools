from django.urls import path, include
from encryption import views

urlpatterns = [
    path('', views.cipherlist, name='encryption-home'),
    path('xor/', views.xor, name='encryption-xor'),
    path('botcrypt/', views.botcrypt, name='encryption-botcrypt'),
]
