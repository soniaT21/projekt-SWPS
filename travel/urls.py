from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:pk>/edit/', views.destination_edit, name='destination_edit'),
    path('<int:pk>/delete/', views.destination_delete, name='destination_delete'),
    path('travelers-summary/', views.traveler_trip_summary, name='traveler_trip_summary'),
    path('<int:pk>/reviews/', views.destination_reviews, name='destination_reviews'),

]

