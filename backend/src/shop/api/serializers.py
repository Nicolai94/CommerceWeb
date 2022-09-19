from shop.models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['user', 'full_name', 'image', 'telephone', 'address']


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = ['title', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Product
        fields = ['title', 'slug', 'category', 'amount', 'image', 'price', 'content', 'created', 'updated', 'active']


class ExhibitedGoodsSerializer(serializers.ModelSerializer):
    exhibited_goods = serializers.CharField(source='product.title')

    class Meta:
        model = ExhibitedGoods
        fields = ['name', 'exhibited_goods']


class SoldGoodsSerializer(serializers.ModelSerializer):
    sold_goods = serializers.CharField(source='product.title')

    class Meta:
        model = SoldGoods
        fields = ['name', 'sold_goods']


class BuyGoodsSerializer(serializers.ModelSerializer):
    buy_goods = serializers.CharField(source='product.title')

    class Meta:
        model = BuyGoods
        fields = ['name', 'buy_goods']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.user')

    class Meta:
        model = Review
        fields = ['name', 'email', 'content', 'created', 'user_name']
