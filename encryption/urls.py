from django.urls import path, include
from encryption import views

urlpatterns = [
    path('', views.cipherlist, name='encryption-home'),
    path('xor/', views.xor_handler, name='encryption-xor'),
    path('botcrypt/', views.botcrypt_handler, name='encryption-botcrypt'),
    path('caesarcipher/', views.caesarcipher_handler, name='encryption-caesarcipher'),
]
