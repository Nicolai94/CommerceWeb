from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shop.api.views import *
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryProductViewSet, basename='categories')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'exhibited_goods', ExhibitedGoodsViewSet, basename='exhibited')
router.register(r'sold_goods', SoldGoodsViewSet, basename='sold')
router.register(r'buy_goods', BuyGoodsViewSet, basename='buy')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

]

urlpatterns+=doc_urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)