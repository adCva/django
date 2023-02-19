from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('update/<str:pk>/', views.updateTask, name="Update"),
    path('delete/<str:pk>/', views.deleteTask, name="Delete")
]

# update dynamic path