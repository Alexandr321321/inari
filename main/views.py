from django.contrib.auth.backends import BaseBackend
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import connection

# Create your views here.
from main.forms import *

def index(request):
    return redirect('products')

def products(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/products.html', context)

def aboutus(request):
    return render(request, 'main/aboutus.html')

# страница пользователя
@login_required
def me(request):
    return render(request, 'main/me.html', {'user': request.user})

# выход
def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    return redirect('login')


# страница входа
def loginPage(request):
    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':

        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)
        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return redirect('main/me.html')
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    return render(request, 'main/login.html', {'form': form})


def catalog(request):
    return render(request, 'main/catalog.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def showProduct(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    user = User.objects.all()
    return render(request, 'main/product.html', {'product': product, 'users': user})

def search(request):
    if request.method == 'POST':
        searchText = request.POST["searchText"]
        product = Product.objects.filter(Q(label__iregex=searchText) | Q(description__iregex=searchText))
        user = User.objects.all()
        context = {
            'products': product,
            'users': user
        }
        return render(request, 'main/search.html', context)

def showPets(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/pets.html', context)


def showElectronics(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/electronics.html', context)


def showClothes(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/clothes.html', context)


def showBooks(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/books.html', context)



def showPharmacy(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/pharmacy.html', context)



def showChildren(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/children.html', context)


def showOther(request):
    product = Product.objects.all()
    user = User.objects.all()
    context = {
        'products': product,
        'users': user
    }
    return render(request, 'main/other.html', context)


@login_required
def addProduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myProducts')
    else:
        form = AddProductForm()
    return render(request, 'main/addproduct.html', {'form': form})


@login_required
def basket(request):
    basket = Basket.objects.all()
    product = Product.objects.all()
    user = User.objects.all()
    sell = Sells.objects.all()
    context = {
        'products': product,
        'users': user,
        'baskets': basket,
        'sells': sell,
    }
    return render(request, 'main/basket.html', context)


@login_required
def addBasket(request, product_id):
    username = request.user.username
    if Basket.objects.filter(username=username, product_id = product_id).exists():
        return redirect('basket')
    form = Basket.objects.create(username=username, product_id = product_id)
    return redirect('basket')


@login_required
def deleteBasket(request, product_id):
    username = request.user.username
    if Basket.objects.filter(username=username, product_id = product_id).exists():
        Basket.objects.filter(username=username, product_id = product_id).delete()
    return redirect('basket')


@login_required
def myProducts(request):
    product = Product.objects.all()
    user = User.objects.all()
    basket = Basket.objects.all()
    context = {
        'products': product,
        'users': user,
        'baskets': basket,
    }
    return render(request, 'main/myProducts.html', context)


@login_required
def deleteProducts(request, product_id):
    username = request.user.username
    if Product.objects.filter(username=username, id = product_id).exists():
        Product.objects.filter(username=username, id = product_id).delete()
    return redirect('myProducts')


@login_required
def deleteUser(request):
    username = request.user.username
    if User.objects.filter(username=username).exists():
        User.objects.filter(username=username).delete()
    return redirect('logout')

@login_required
def addAuctionBid(request, product_id):
    if request.method == 'POST':
        form = AddAuctionBid(request.POST)
        for p in Product.objects.raw("SELECT * FROM main_product WHERE id = %s", [product_id]):
            correct_auction = p.auction
            correct_price = p.price
        if form.is_valid() and int(form.cleaned_data['bid']) > int(correct_auction) and int(form.cleaned_data['bid']) < int(correct_price):
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM main_basket WHERE product_id = %s" % (product_id))
                cursor.execute("INSERT INTO main_basket (username, product_id) VALUES (%s, %s)" % (request.user.username, product_id))
                cursor.execute("UPDATE main_product SET auction = %s WHERE id = %s" % (form.cleaned_data['bid'], product_id))
            return redirect('products')
        return redirect('products')
    else:
        return redirect('products')

@login_required
def sellProduct(request, product_id):
    if request.method == 'POST':
        for p in Product.objects.raw("SELECT * FROM main_product WHERE id = %s", [product_id]):
            correct_username = p.username
            correct_auction = p.auction
            correct_price = p.price
            correct_status = 0
        for b in Basket.objects.raw("SELECT * FROM main_basket WHERE product_id = %s", [product_id]):
            correct_buyer = b.username
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO main_sells (username, product_id, buyer, price, auction, status) VALUES (%s, %s, %s, %s, %s, %s)" % (correct_username, product_id, correct_buyer, correct_price, correct_auction, correct_status))
            cursor.execute("UPDATE main_product SET status = 1 WHERE id = %s" %  product_id)
    return redirect('products')

@login_required
def buyProductAuction(request, product_id):
    username = request.user.username
    if request.method == 'POST':
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [username]):
            correct_balance = user.balance
        for product in Product.objects.raw("SELECT * FROM main_product WHERE id = %s", [product_id]):
            correct_auction = product.auction
            correct_seller_username = product.username
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [correct_seller_username]):
            correct_seller_balance = user.balance
        if int(correct_auction) <= int(correct_balance):
            buyer_new_balance = int(correct_balance) - int(correct_auction)
            seller_new_balance = int(correct_seller_balance) + int(correct_auction)
            with connection.cursor() as cursor:
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (buyer_new_balance, username))
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (seller_new_balance, correct_seller_username))
                cursor.execute("UPDATE main_sells SET status = 1 WHERE product_id = %s" % product_id)
                cursor.execute("DELETE FROM main_basket WHERE product_id = %s" % product_id)
        return redirect('purchases')
    return redirect('products')

@login_required
def buyProductPrice(request, product_id):
    username = request.user.username
    if request.method == 'POST':
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [username]):
            correct_balance = user.balance
        for product in Product.objects.raw("SELECT * FROM main_product WHERE id = %s", [product_id]):
            correct_price = product.price
            correct_seller_username = product.username
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [correct_seller_username]):
            correct_seller_balance = user.balance
        if int(correct_price) <= int(correct_balance):
            buyer_new_balance = int(correct_balance) - int(correct_price)
            seller_new_balance = int(correct_seller_balance) + int(correct_price)
            with connection.cursor() as cursor:
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (buyer_new_balance, username))
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (seller_new_balance, correct_seller_username))
                cursor.execute("UPDATE main_sells SET status = 1 WHERE product_id = %s" % product_id)
                cursor.execute("DELETE FROM main_basket WHERE product_id = %s" % product_id)
        return redirect('purchases')
    return redirect('products')

@login_required
def purchases(request):
    basket = Basket.objects.all()
    product = Product.objects.all()
    user = User.objects.all()
    sell = Sells.objects.all()
    context = {
        'products': product,
        'users': user,
        'baskets': basket,
        'sells': sell,
    }
    return render(request, 'main/purchases.html', context)

@login_required
def upBalance(request):
    username = request.user.username
    if request.method == 'POST':
        form = UpBalance(request.POST)
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [username]):
            correct_balance = user.balance
        if form.is_valid() and int(form.cleaned_data['up_balance']) > 0:
            with connection.cursor() as cursor:
                correct_balance = int(correct_balance) + int(form.cleaned_data['up_balance'])
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (correct_balance, username))
        return redirect('me')
    else:
        form = UpBalance()
    return render(request, 'main/upbalance.html', {'form': form})

@login_required
def downBalance(request):
    username = request.user.username
    if request.method == 'POST':
        form = DownBalance(request.POST)
        for user in User.objects.raw("SELECT * FROM main_user WHERE username = %s", [username]):
            correct_balance = user.balance
        if form.is_valid() and int(form.cleaned_data['down_balance']) > 0 and int(form.cleaned_data['down_balance']) <= int(correct_balance):
            with connection.cursor() as cursor:
                correct_balance = int(correct_balance) - int(form.cleaned_data['down_balance'])
                cursor.execute("UPDATE main_user SET balance = %s WHERE username = %s" % (correct_balance, username))
        return redirect('me')
    else:
        form = DownBalance()
    return render(request, 'main/downbalance.html', {'form': form})