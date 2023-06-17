"""mysite6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path, include
from main import views
from main.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='home'),
    re_path(r'aboutus', views.aboutus, name='aboutus'),
    re_path(r'login', views.loginPage, name='login'),
    re_path(r'register', views.register, name='register'),
    re_path(r'products', views.products, name='products'),
    re_path(r'catalog', views.catalog, name='catalog'),
    re_path(r'me', views.me, name='me'),
    re_path(r'logout', views.doLogout, name='logout'),
    re_path(r'product/(?P<product_id>[0-9]+)/$', views.showProduct, name='product'),
    re_path(r'search', views.search, name='search'),
    re_path(r'pets', views.showPets, name='pets'),
    re_path(r'electronics', views.showElectronics, name='electronics'),
    re_path(r'clothes', views.showClothes, name='clothes'),
    re_path(r'books', views.showBooks, name='books'),
    re_path(r'pharmacy', views.showPharmacy, name='pharmacy'),
    re_path(r'children', views.showChildren, name='children'),
    re_path(r'other', views.showOther, name='other'),
    re_path(r'addproduct', views.addProduct, name='addProduct'),
    re_path(r'basket', views.basket, name='basket'),
    re_path(r'addBasket/(?P<product_id>[0-9]+)/$', views.addBasket, name='addBasket'),
    re_path(r'deleteBasket/(?P<product_id>[0-9]+)/$', views.deleteBasket, name='deleteBasket'),
    re_path(r'deleteUser', views.deleteUser, name='deleteUser'),
    re_path(r'myPoducts', views.myProducts, name='myProducts'),
    re_path(r'deleteProducts/(?P<product_id>[0-9]+)/$', views.deleteProducts, name='deleteProducts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)