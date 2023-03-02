from django.shortcuts import render, redirect
from users.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/users/login')
            else:
                form.add_error('password1', 'пароли не совпадают')

        return render(request, 'users/register.html', context={
            'form': form
        })


def login_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }

        return render(request, 'users/login.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            """ authenticate """
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                """ authorization """
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('username', 'Пользователь не найден!')

        return render(request, 'users/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('/products')
