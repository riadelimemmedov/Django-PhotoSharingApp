from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import *

# Create your views here.
#!SignUpView
class SignUpView(CreateView):
    form_class = SignUpUserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('photoapp:listphotos')
    
    def form_valid(self,form):
        to_return = super().form_valid(form)
        
        user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password1'))
        login(self.request,user)
        return to_return

#!CustomLoginView
class SignInView(LoginView):
    template_name = 'users/signin.html'
    