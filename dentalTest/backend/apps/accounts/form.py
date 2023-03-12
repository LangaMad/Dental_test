
from django import forms
from .models import User,Doctor
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm



class UserLoginForm(forms.Form):
    name = forms.CharField(
        label="name",
        widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Имя"})
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Почта"})
    )
    phone = forms.EmailField(
        label="Номер",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Номер"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-input",
                "placeholder":"Пароль"
            }
            )
    )




class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Пароль"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Повторите пароль"}))

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Никнейм"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Никнейм"}))

    age = forms.IntegerField(widget=forms.IntegerField(attrs={"class": "form-input", "placeholder": "Никнейм"}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-input", "placeholder": "Почта"}))


    class Meta:
        model = User
        fields = [
            'name',
            'last_name',
            'email',
        ]



class DoctorRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Пароль"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input","placeholder":"Повторите пароль"}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Никнейм"})
    )

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-input", "placeholder": "Почта"}))

    class Meta:
        model = Doctor
        fields = [
            'name',
            'email',
        ]


class DoctorLoginForm(forms.Form):
    name = forms.CharField(
        label="name",
        widget=forms.TextInput(attrs={"class":"form-input","placeholder":"Имя"})
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Почта"})
    )
    phone = forms.EmailField(
        label="Номер",
        widget=forms.EmailInput(attrs={"class":"form-input","placeholder":"Номер"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-input",
                "placeholder":"Пароль"
            }
            )
    )

