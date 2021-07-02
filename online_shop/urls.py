from django.contrib import admin
from django.urls import path, include
from online_shop.views import *

app_name = 'product'
urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('product/detail/<int:pk>', ProductDetailView.as_view()),
    path('product/all', ProductsListView.as_view()),
    path('product/<int:pk>/add', BasketCreateView.as_view()),
    path('basket', BasketListView.as_view()),
    path('basket/<int:pk>', BasketDetailView.as_view()),
]