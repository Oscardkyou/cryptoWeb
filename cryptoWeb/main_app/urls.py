from django.urls import path
from .views import index_view, index_view3, index_view4, index_view2

urlpatterns = [
    path('', index_view),
    path('index/', index_view2),
    path('index3/', index_view3),
    path('index4/', index_view4),
]

