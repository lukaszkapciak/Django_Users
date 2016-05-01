from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import (
login,
logout,
get_user_model,
authenticate
)
from django.shortcuts import redirect

# Create your views here.

def LoginUserFormView(request):
    form = LoginUserForm(request.POST or None)
    title = 'Login'
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/books')
    return render(request, 'form.html', {'form':form, 'title':title})



def LogoutUserFormView(request):
    title = 'Logout'
    logout(request)
    return redirect('/books')


def RegisterUserFormView(request):
    form = RegisterUserForm(request.POST or None)
    title = 'Register Now'
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect('/books')
    return render(request, 'form.html', {'form':form, 'title':title})


def MyaccountView(request):
    form = request.user
    title = "My account"
    if form.is_authenticated():
        return render(request, 'myaccount.html', {'form':form, 'title':title})
    return redirect('/books')