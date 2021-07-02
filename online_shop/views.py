from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from online_shop.serializers import *
from online_shop.models import *
from online_shop.permissions import IsOwnerOrReadOnly


class CreateUserView(generics.CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (IsAdminUser, )
    queryset = Product.objects.all()


class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketDetailSerializer


class BasketListView(generics.ListAPIView):
    serializer_class = BasketDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        current_user = self.request.user
        print(current_user)
        return Basket.objects.filter(user=current_user)


class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketDetailSerializer
    queryset = Basket.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
