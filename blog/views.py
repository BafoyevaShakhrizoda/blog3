from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=name).exists():
            messages.error(request, 'Bu username band.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu email band.')
            return redirect('register')


        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()

        messages.success(request, 'Profil yaratildi! Endi tizimga kiring.')
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')


        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username yoki parol noto‘g‘ri')
            return redirect('login')

    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')
