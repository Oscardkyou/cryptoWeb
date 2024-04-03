from django.urls import path, re_path
from cats import views

urlpatterns = [
    path('', views.index),
    path('dogs/<int:dog_id>/', views.categories),
    path('dogs/<slug:dog_slug>/', views.categories_by_slug),
    re_path(r"^acrhive/(?P<year>[0-9]{4}/)", views.acrhive)
]
