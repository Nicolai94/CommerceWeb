from django_filters import rest_framework as filters

from shop.models import Product


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter()
    min_price = filters.NumberFilter(field_name='price', lookup_expr='lt')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='gt')

    class Meta:
        model = Product
        fields = ['title', 'price', 'min_price', 'max_price', 'active', 'category', 'amount']