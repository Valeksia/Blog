from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('blogs:home')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def custom_login(request):
    """Обрабатывает вход пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму входа.
        form = AuthenticationForm()
    else:
        # Обработка заполненной формы.
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blogs:home')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'users/login.html', context)