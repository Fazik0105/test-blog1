from django.urls import path, include

from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', test,name='test'),
    path('genre/<int:pk>', get_genre,name='genre'),
]