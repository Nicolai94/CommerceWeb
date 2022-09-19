from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'slug', 'price', 'get_photo', 'active')
    list_filter = ['price', 'created']
    list_editable = ['price', 'active']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}
    save_on_top = True
    save_as = True
    actions = ['publish', 'unpublish']
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url }" width="50">')
        return '-'


    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == int(1):
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == int(1):
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    get_photo.short_description = 'Mark'

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'telephone', 'get_photo')
    list_filter = ['user', 'full_name']
    search_fields = ['user']
    save_on_top = True
    save_as = True
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url }" width="50">')
        return '-'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'content', 'created', 'user']
    list_filter = ['user', 'created']
    search_fields = ['user', 'content']
    save_on_top = True
    save_as = True
    readonly_fields = ['created']


@admin.register(ExhibitedGoods)
class ExhibitedGoods(admin.ModelAdmin):
    list_display = ['name', 'product']
    list_filter = ['product']
    search_fields = ['name', 'product']


@admin.register(SoldGoods)
class SoldGoods(admin.ModelAdmin):
    list_display = ['name', 'product']
    list_filter = ['product']
    search_fields = ['name', 'product']


@admin.register(BuyGoods)
class BuyGoods(admin.ModelAdmin):
    list_display = ['name', 'product']
    list_filter = ['product']
    search_fields = ['name', 'product']


admin.site.site_title = 'DjangoReact'
admin.site.site_header = 'DjangoReact'