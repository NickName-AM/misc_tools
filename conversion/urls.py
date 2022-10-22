from django.urls import path, include
from conversion import views

urlpatterns = [
    path('', views.home, name='conversion-home'),
    path('numtoroman/', views.num_to_roman, name='num-to-roman')
]
