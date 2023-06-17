from django.contrib.auth.backends import BaseBackend
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    context = {
        'products': product,
        'users': user,
        'baskets': basket,
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
    context = {
        'products': product,
        'users': user,
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