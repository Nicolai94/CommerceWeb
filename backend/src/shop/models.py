from django.contrib.auth.models import User
from django.db import models


class CategoryProduct(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    content = models.TextField(null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Опцбликовано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    amount = models.SmallIntegerField(default=0, verbose_name='Количество')
    active = models.BooleanField(default=True, verbose_name='Черновик')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']


class ExhibitedGoods(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Выставленный товар'
        verbose_name_plural = 'Выставленные товары'
        ordering = ('created',)


class SoldGoods(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'
        ordering = ('created',)


class BuyGoods(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Купленный товар'
        verbose_name_plural = 'Купленные товары'
        ordering = ('created',)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50, verbose_name='Полное имя')
    telephone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    image = models.ImageField(upload_to='admins', verbose_name='Изображение')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
    date_reg = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    favorite = models.ManyToManyField(Product, verbose_name='Избранное', related_name='favorite_product', blank=True, default=None)
    buy_goods = models.ForeignKey(BuyGoods, on_delete=models.SET_NULL, blank=True, null=True)
    exhibited_goods = models.ForeignKey(ExhibitedGoods, on_delete=models.SET_NULL, blank=True, null=True)
    sold = models.ForeignKey(SoldGoods, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль пользователя'

    def __str__(self):
        return "{} пользователь".format(self.user.__str__())


class Review(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(max_length=600, verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('created',)
