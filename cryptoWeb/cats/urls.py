from django.urls import path, re_path, register_converter
from . import views, converter


#register_converter(converter.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    #path('dogs/<int:dog_id>/', views.categories, name='dogs_id'),
    #path('dogs/<slug:dog_slug>/', views.categories_by_slug, name='dogs'),
    #path("archive/<int:year>/", views.archive, name='archive')
]
