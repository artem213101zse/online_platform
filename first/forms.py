from django import forms
from django.contrib.auth.models import User


class GeoForm(forms.Form):
    latitude = forms.FloatField(
        label='Широта',
        required=True,
        max_value=1000,
        min_value=0,
        widget=forms.HiddenInput(
            attrs={
                'id': 'latitude',
            }
        )
    )
    longitude = forms.FloatField(
        label='Долгота',
        required=True,
        max_value=1000,
        min_value=0,
        widget=forms.HiddenInput(
            attrs={
                'id': 'longitude',
            }
        )
    )
    altitude = forms.FloatField(
        label='Высота',
        required=True,
        widget=forms.HiddenInput(
            attrs={
                'id': 'altitude',
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Логин'
            }
        )

    )
    password = forms.CharField(
        label="Пароль",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль'
            }
        ))

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={' placeholder': 'Придумайте логин' }))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={' placeholder': 'Ваше имя'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={' placeholder': 'Ваша фамилия'}))
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={' placeholder': 'Электронная почта'}))

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={' placeholder': 'Пароль' }))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={' placeholder': 'Повторите пароль' }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
            messages.success(request, "Вы успешно зарегистрировались. Теперь Вы можете войти в систему")
        return cd['password2']