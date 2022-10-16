from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import MyUser

# Create your views here.

allowed_themes = ('light', 'dark')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd1 = request.POST['password1']
        passwd2 = request.POST['password2']
        email = request.POST['email']
        my_theme = request.POST['theme']
        if my_theme not in allowed_themes:
            my_theme = 'dark'
        if passwd1 == passwd2:
            uza = User.objects.create_user(username=uname, email=email, password=passwd1)
            MyUser.objects.create(user=uza, theme=my_theme)

            messages.success(request, f'{uname} created.')
        else:
            messages.success(request, f'{uname} creation failed.')
        
        return redirect('user-signin')
    else:
        return render(request, 'users/register.html')

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
        mytheme = user.myuser.theme
        try:
            theme = request.POST['theme']
            if theme not in allowed_themes:
                theme = mytheme
        except:
            theme = mytheme
        if theme != mytheme:
            u = MyUser.objects.get(user=user)
            u.theme = theme
            u.save()
            messages.success(request, 'Theme changed successfully')
            return redirect('user-profile')

        if user.check_password(old_passwd):
            if new_passwd != old_passwd and len(new_passwd) > 0 and len(uname) > 0:
                try:
                    
                    user.username = uname
                    user.set_password(new_passwd)
                    user.save()
                    
                    messages.success(request, 'Successfully changed')
                    return redirect('user-signin')
                except:
                    messages.error(request, 'Could not change profile!')
                    return redirect('user-profile')
            else:
                messages.error(request, 'Could not change profile!')
                return redirect('pgen-home')
        else:
            messages.error(request, 'Wrong password')
            return redirect('user-profile')