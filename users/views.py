from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} created.')
            return redirect('user-signin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html')
    elif request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request, username=uname, password=passwd)
            # 'user' is not a boolen value, its a user
        if user:
            # IF user exists and is authenticated, log him/her in and return to home
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('pgen-home')
        else:
            messages.error(request, 'Something\'s wrong. I can feel it.')
            return redirect('user-signin')

@login_required
def signout(request):
    logout(request)
    return redirect('pgen-home')

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    
    if request.method == 'GET':
        return render(request, 'users/profile.html', {'user': user})
    elif request.method == 'POST':
        uname = request.POST['username']
        new_passwd = request.POST['newpassword']
        old_passwd = request.POST['oldpassword']
        if user.check_password(old_passwd):
            if new_passwd != old_passwd and len(new_passwd) > 0 and len(uname) > 0:
                try:
                    user.username = uname
                    user.set_password(new_passwd)
                    user.save()
                    messages.success(request, 'Successfully changed')
                    return redirect('user-sigin')
                except:
                    messages.error(request, 'Could not change profile!')
                    return redirect('user-profile')
            else:
                messages.error(request, 'Could not change profile!')
                return redirect('pgen-home')
        else:
            messages.error(request, 'Wrong password')
            return redirect('user-profile')