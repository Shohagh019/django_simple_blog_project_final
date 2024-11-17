from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request,'author.html', {'form':author_form})

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your Account Created Successfully!')
            return redirect('register')
    else:
        form = forms.RegisterForm()
    return render(request, 'register.html', {'form': form, 'type': 'Register'})        

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully!')
                login(request, user)
                return redirect('register')
            else:
                messages.warning(request, 'Incorrect Login Information!')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html',{'form': form, 'type': 'Login'})            

@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.UpdateUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile Updated Successfully!')
            return redirect('profile')
    else:
        form = forms.UpdateUserData(instance = request.user)
    return render(request, 'profile.html', {'form':form})    


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your Password Changed Successfully!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': form}) 