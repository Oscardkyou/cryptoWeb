from django.contrib import admin
from django.urls import path, include
from main_app.views import index_view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('index/', index_view2)
]
