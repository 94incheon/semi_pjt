from django.urls import path
from . import views

# /reviews/
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('detail/<int:pk>/', views.detail),
    path('update/<int:pk>/', views.update),
    path('apply_update/<int:pk>/', views.apply_update),
    path('delete/<int:pk>/', views.delete),
]