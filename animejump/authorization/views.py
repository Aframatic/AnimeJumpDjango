from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm, AuthenticationForm
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Логин или пароль введены не верно')
                return redirect('login')
        else:
            messages.error(request, 'Логин или пароль введены не верно')
    return render(request, 'authorization/login.html')


def user_registr(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            username = request.POST['login']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                User.objects.create_user(email=email, username=username, password=password)
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                return render(request, 'authorization/login.html')
            else:
                messages.error(request, 'Пароли не совпадают')
                return redirect('registration')
    else:
        form = SignUpForm()

    data = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authorization/registration.html', data)


def user_logout(request):
    logout(request)
    return redirect('login')
