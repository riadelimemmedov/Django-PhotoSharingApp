from django.shortcuts import render,get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy

from .models import *

# Create your views here.

#!PhotoListView
class PhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'

#!PhotoTagListView
class PhotoTagListView(PhotoListView):
    template_name = 'photoapp/taglist.html'
    
    #find tags input url
    def get_tag(self):
        print('slug value ', self.kwargs.get('slug'))#return none
        print('tag value ', self.kwargs.get('tag'))#return tag value from url,we used value except than key
        print('Working get_tag method ', self.kwargs.get('tag'))
        return self.kwargs.get('tag')

    #return photos matched input tags
    def get_queryset(self):
        print('Working get_queryset method')
        return self.model.objects.filter(tags__slug=self.get_tag())
    
    #tags passed to context
    def get_context_data(self,**kwargs):
        print('Isledi get_context_data function')
        context = super(PhotoTagListView,self).get_context_data(**kwargs)
        context['tag'] = self.get_tag()
        return context 

#!PhotoDetailView
class PhotoDetailView(LoginRequiredMixin,DetailView):
    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'
    # slug_url_kwarg = 'slug'
    
    def get_object(self,queryset=None):
        return get_object_or_404(Photo,slug=self.kwargs.get('slug'))

#!PhotoCreateView
class PhotoCreateView(CreateView):
    model = Photo
    fields = ['title','description','image','tags']
    template_name = 'photoapp/create.html'
    success_url = reverse_lazy('photoapp:listphotos')
    
    def form_valid(self,form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
    

#*UserIsSubmitter
class UserIsSubmitter(UserPassesTestMixin):
    #UserPassesTestMixin => CBV Mixin that allows you to define a test function which must return True,if the current user can access the view.
    
    #Custom Method
    def get_photo(self):
        return get_object_or_404(Photo,pk=self.kwargs.get('pk'))
    
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')

#!PhotoUpdateView
class PhotoUpdateView(UserIsSubmitter,UpdateView):
    model = Photo
    template_name = 'photoapp/update.html'
    fields = ['title','description','tags']
    context_object_name = 'photo'
    success_url = reverse_lazy('photoapp:listphotos')

#!PhotoDeleteView
class PhotoDeleteView(UserIsSubmitter,DeleteView):
    model = Photo
    template_name = 'photoapp/delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('photoapp:listphotos')