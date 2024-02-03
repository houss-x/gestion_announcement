from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def user_list(request):
    users = User.objects.exclude(is_superuser=True)


    return render(request, 'admin.html', {'users': users})

def toggle_user_status(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('authentication:adminportail')

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  
                request.session['user_id'] = user.id
                if user.is_superuser:
                    return redirect('authentication:adminportail')
                else:
                    return redirect('anouncement:anouncement_list')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    
    logout(request)
    return redirect('login')