from django.urls import path
from cats import views

urlpatterns = [
    path('', views.index),
    path('dogs/<int:dog_id>/', views.categories),
    path('dogs/<slug:dog_slug>/', views.categories_by_slug),
]
