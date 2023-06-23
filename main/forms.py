from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import *


# форма авторизации
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Phone number')
    password = forms.CharField(required=True, label='Пароль')


# форма регистрации
class UserCreationForm(BaseUserCreationForm):
    nickname = forms.CharField(required=True, label='nickname')
    email = forms.CharField(required=True, label='email')
    second_name = forms.CharField(required=True, label='second_name')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nickname', 'email', 'last_name', 'first_name', 'second_name', 'usertype')

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        # валидация паролей
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(
                {'password_confirm': "Пароли не совпадают", 'password': ''}
            )
        # валидация телефона
        username = self.cleaned_data.get("username")
        # валидация никнейма
        nickname = self.cleaned_data.get("nickname")

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Такой телефон уже занят"})

        if get_user_model().objects.filter(nickname=nickname).exists():
            raise forms.ValidationError({'nickname': "Такой никнейм уже занят уже занят"})

        # валидация email
        try:
            validate_email(self.cleaned_data.get("email"))
        except ValidationError as e:
            raise forms.ValidationError({'email': "Email не является валидным адресом"})

        return cleaned_data


# форма добавления товара
class AddProductForm(forms.ModelForm):
    username = forms.CharField(required=True, label='username')
    label = forms.CharField(required=True, label='label')
    description = forms.CharField(required=True, label='description')
    auction = forms.CharField(required=True, label='auction')
    price = forms.CharField(required=True, label='price')
    category = forms.CharField(required=True, label='category')
    image = forms.FileField(required=True, label='image')

    class Meta:
        model = Product
        fields = ('username', 'label', 'description', 'auction', 'price', 'category', 'image')


class AddAuctionBid(forms.Form):
    bid = forms.CharField(required=True, label='bid')

class UpBalance(forms.Form):
    up_balance = forms.CharField(required=True, label='up_balance')

class DownBalance(forms.Form):
    down_balance = forms.CharField(required=True, label='down_balance')