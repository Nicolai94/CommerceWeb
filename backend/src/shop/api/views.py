from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from djreact.service import ProductFilter
from shop.models import *

from shop.api.serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'title']
    search_fields = ['title']
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'price', 'category']
    ordering_fields = ['title', 'id']
    ordering = ['id']
    permission_classes = [permissions.AllowAny]


class ExhibitedGoodsViewSet(viewsets.ModelViewSet):
    queryset = ExhibitedGoods.objects.all().order_by('-id')
    serializer_class = ExhibitedGoodsSerializer
    permission_classes = [permissions.AllowAny]


class SoldGoodsViewSet(viewsets.ModelViewSet):
    queryset = SoldGoods.objects.all().order_by('-id')
    serializer_class = SoldGoodsSerializer
    permission_classes = [permissions.AllowAny]


class BuyGoodsViewSet(viewsets.ModelViewSet):
    queryset = BuyGoods.objects.all().order_by('-id')
    serializer_class = BuyGoodsSerializer
    permission_classes = [permissions.AllowAny]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
