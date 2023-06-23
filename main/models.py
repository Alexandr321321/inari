from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(error_messages={'unique': 'Пользователь с таким телефоном уже существует!'}, help_text='15 символов. Только цифры',max_length=15, unique=True, verbose_name='phone')
    nickname = models.CharField(error_messages={'unique': 'Пользователь с таким никнеймом уже существует!'}, max_length=20, unique=True, verbose_name='nickname')
    second_name = models.CharField(max_length=150, verbose_name='second name')
    email = models.EmailField(max_length=254, verbose_name='email address', unique=True, error_messages={'unique': 'Пользователь с такой почтой уже существует!'})
    balance = models.CharField(max_length=10, help_text='Баланс', verbose_name='money', default=0)
    user_type_choises =(('buyer', 'Я покупатель'),
               ('seller', 'Я продавец'))
    usertype = models.CharField(max_length=15, blank=False, choices=user_type_choises, default='buyer', help_text='Usertype', verbose_name='usertype')


class Product(models.Model):
    username = models.CharField(help_text='15 символов. Только цифры', max_length=15, verbose_name='phone of seller')
    label = models.TextField(max_length=30, help_text='От 5 до 30 символов. Название товара.', verbose_name='name')
    description = models.TextField(max_length=500, help_text='От 5 до 500 символов. Название товара.', verbose_name='description')
    price = models.CharField(max_length=10, help_text='Стоймость товара.', verbose_name='price')
    auction = models.CharField(max_length=10, help_text='Аукционная стоймость товара.', verbose_name='auction')
    category_choises = (('pets', 'Товары для животных'),
                        ('electronics', 'Электроника'),
                        ('clothes', 'Одежда'),
                        ('books', 'Книги'),
                        ('pharmacy', 'Аптека'),
                        ('children', 'Детские товары'),
                        ('other', 'Другое'),)
    category = models.CharField(max_length=30, blank=False, choices=category_choises, default='Другое', verbose_name='category')
    image = models.FileField(help_text='Изображение товара', verbose_name='image')
    status = models.BooleanField(help_text='Продаётся/Не продаётся', default=0)


class Basket(models.Model):
    username = models.CharField(help_text='15 символов. Только цифры', max_length=15, verbose_name='phone of seller')
    product_id = models.IntegerField(help_text='id товара', verbose_name='id product')


class Sells(models.Model):
    username = models.CharField(help_text='15 символов. Только цифры', max_length=15, verbose_name='phone of seller')
    product_id = models.IntegerField(help_text='id товара', verbose_name='id product')
    buyer = models.CharField(help_text='15 символов. Только цифры', max_length=15, verbose_name='phone of seller')
    price = models.CharField(max_length=10, help_text='Стоймость товара.', verbose_name='price')
    auction = models.CharField(max_length=10, help_text='Аукционная стоймость товара.', verbose_name='auction')
    status = models.BooleanField(help_text='Статус заказа', default=0)

