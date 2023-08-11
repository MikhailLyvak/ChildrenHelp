from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You might add more logic here, like sending confirmation emails
            return redirect('test_app:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('charity:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


@login_required
def profile_view(request):
    username = request.user.username
    phone = request.user.phone
    
    context = {
        "username": username,
        "phone": phone,
    }
    return render(request, 'registration/profile.html', context=context)
