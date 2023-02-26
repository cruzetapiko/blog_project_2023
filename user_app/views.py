from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from django.contrib import messages

@login_required
def profile(request):
    return render(request, 'user_app/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account has been created {username}!')
            return redirect('user_app-login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_app/register.html', {'form': form})