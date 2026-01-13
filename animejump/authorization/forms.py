from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Почта',
                             required=True,
                             max_length=30,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             error_messages={
                                 'required': 'Поле обязательно',
                                 'max_length': 'Максимум 30 символов',
                             })
    login = forms.CharField(label='Логин',
                            required=True,
                            max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={
                                'required': 'Поле обязательно',
                                'max_length': 'Максимум 30 символов',
                            })
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               required=True,
                               min_length=8,
                               max_length=30,
                               error_messages={
                                   'required': 'Поле обязательно',
                                   'max_length': 'Максимум 30 символов',
                                   'min_length': 'Минимум 8 символов',
                               })
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput,
                                required=True,
                                min_length=8,
                                max_length=30,
                                error_messages={
                                    'required': 'Поле обязательно',
                                    'max_length': 'Максимум 30 символов',
                                    'min_length': 'Минимум 8 символов',
                                })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'registrationEmail',
            'placeholder': 'Почта',
        })
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'id': 'registrationLogin',
            'placeholder': 'Логин',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'registrationPassword',
            'placeholder': 'Пароль',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'registrationConfirmPassword',
            'placeholder': 'Подтверждение пароля',
        })

    class Meta:
        model = User
        fields = ('email', 'login', 'password')


class LoginForm(forms.Form):
    login = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
