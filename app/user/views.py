from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password

from .forms import LoginUserForm, CreateUserForm, CustomUserChange, UpdateUser


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {'form': LoginUserForm})

    def post(self, request):
        form = LoginUserForm(data=request.POST)
        # check to see first if the form is valid
        if form.is_valid():
            # authenticate using form's cleaned_data
            user = authenticate(
                request, 
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            # if user is non-existent or not active, return invalid creds
            if user is None or not user.is_active:
                messages.error(request, 'Username or Password is incorrect')
                return render(
                    request,
                    'login.html',
                    {'form': LoginUserForm}
                )

            if not form.cleaned_data.get('remember_me'):
                request.session.set_expiry(0)

            login(request, user)

            # redirect to home if login is successful
            return redirect('/journals/')
            
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)

        return redirect('/login/')


class SignUpView(View):

    def get(self, request):
        return render(request, 'signup.html', {'form': CreateUserForm})

    def post(self, request):
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
        return render(request, 'signup.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'login_required'


    def get(self, request):
        return render(request, 'profile.html', {'form': UpdateUser})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = UpdateUser(data=request.POST, instance=user)
        if form.is_valid():
            # check if passwords are provided, if so, check and change its passowrd
            if form.cleaned_data['current_password'] and form.cleaned_data['new_password']:
                # ensure first if new name is provided to avoid saving of blank name
                if form.cleaned_data['name']:
                    form.save()
                # assign new password
                if user.check_password(form.cleaned_data['current_password']):
                    user.set_password(form.cleaned_data['new_password'])

            if form.cleaned_data['name']:
                    form.save()

            return render(request, 'profile.html', {'form': form})

        return render(request, 'profile.html', {'form': form})
    