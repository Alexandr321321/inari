from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname', 'email', 'usertype')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('label', 'id', 'username', 'price', 'category')

class BasketAdmin(admin.ModelAdmin):
    list_display = ('username', 'product_id')

class SellsAdmin(admin.ModelAdmin):
    list_display = ('username', 'product_id', 'buyer', 'price', 'auction')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Sells, SellsAdmin)