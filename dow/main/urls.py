from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data/', views.data_list, name='data_list'),
    path('data/create/', views.data_create, name='data_create'),
    path('data/<int:pk>/', views.data_detail, name='data_detail'),
    path('data/<int:pk>/edit/', views.data_update, name='data_update'),
    path('data/<int:pk>/delete/', views.data_delete, name='data_delete'),
]