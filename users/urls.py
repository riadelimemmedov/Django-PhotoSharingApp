from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

app_name='users'
urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('signin/',SignInView.as_view(),name='signin'),
    path('logout/',LogoutView.as_view(),name='logout')
]
