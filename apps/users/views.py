from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile, Seller
from .forms import ProfileForm, SellerForm, UserForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})


def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_form.html', {'form': form})


def seller_create(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = SellerForm()
    return render(request, 'users/seller_form.html', {'form': form})
