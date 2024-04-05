from django.contrib import admin
from django.urls import path, include
from cats.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('context/', include('main_app.urls')),
    path('posts/', include('posts.urls')),
    path('', include('cats.urls')),
]


handler404 = page_not_found