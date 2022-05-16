from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings



urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('filter-category/', CategoryFilter.as_view()),
    path('user/', UserDetailView.as_view()),
    path('wishlist/', WishlistView.as_view()),
    
]