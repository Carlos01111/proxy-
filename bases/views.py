from multiprocessing import context
from django.shortcuts import render
#vistas genericas
from django.views.generic import ListView, DetailView

#models
from bases.models import Post, PostContent
# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    model= Post
    context_object_name= 'posts'
    

    
class DetailPostView(DetailView):
    template_name = 'detailpost.html'
    model = Post
    context_object_name = 'posts'
    
    