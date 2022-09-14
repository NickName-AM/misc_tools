from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('edit/<int:n_id>/', views.edit,name='edit'),
    path('add/', views.add, name='add'),
    path('delete/<int:n_id>/', views.delete, name='delete'),
]
