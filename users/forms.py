from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpUserForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(SignUpUserForm,self).__init__(*args,**kwargs)
        for field in ['username', 'password1','password2']:
            self.fields[field].help_text = None