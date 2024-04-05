from django.urls import path, re_path, register_converter
from . import views, converter


register_converter(converter.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('dogs/<int:dog_id>/', views.categories, name='dogs_id'),
    path('dogs/<slug:dog_slug>/', views.categories_by_slug, name='dogs'),
    path("archive/<year4:year>/", views.archive, name='archive')
]
