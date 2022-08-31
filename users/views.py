from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
#!SignUpView
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('photoapp:listphotos')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None
    
    def form_valid(self,form):
        # to_return = super().form_valid(form)
        
        user = authenticate(username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password1'))
        login(self.request,user)
        return super(SignUpView,self).form_valid(form)

#!CustomLoginView
class SignInView(LoginView):
    template_name = 'users/signin.html'
    