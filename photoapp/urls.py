from django.urls import path
from .views import *

app_name = 'photoapp'
urlpatterns = [
    path('',PhotoListView.as_view(),name='listphotos'),
    path('tag/<slug:tag>/',PhotoTagListView.as_view(),name='taglist'),
    path('photo/<slug:slug>/',PhotoDetailView.as_view(),name='photodetail'),
    path('photo/create/',PhotoCreateView.as_view(),name='photocreate'),
    path('photo/update/<int:pk>/',PhotoUpdateView.as_view(),name='photoupdate'),
    path('photo/delete/<int:pk>/',PhotoDeleteView.as_view(),name='photodelete')
]
