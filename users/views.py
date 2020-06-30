from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    

    if request.method=='POST':
        print('this is post')
        if request.method == 'POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('users:login')
    else:
        form = SignUpForm()
    context={'form':form}
    print(form.errors)
    return render(request,'register.html',context)



def forgotUser(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'forgot.html', {
        'form': form
    })


def loginfn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            print('not none')
            login(request, user)
            return redirect('tester:home')
        else:
            messages.info(request,'Username or Password is incorrect. Please try again')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('users:login')
