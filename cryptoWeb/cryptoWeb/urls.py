from django.contrib import admin
from django.urls import path, include
from main_app.views import index_view2, index_view3, index_view4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('context/', include('main_app.urls')),
    path('posts/', include('posts.urls')),
]
