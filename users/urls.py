from django.urls import path, include
from users import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('signin/', views.signin, name='user-signin'),
    path('signout/', views.signout, name='user-signout'),
    path('profile/', views.profile, name='user-profile')
]
