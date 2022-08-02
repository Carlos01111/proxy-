from multiprocessing import context
from typing import List
from django.shortcuts import render
#vistas genericas
from django.views.generic import ListView, DetailView

#models
from bases.models import Category, Post, Subcategory
# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    model= Post
    context_object_name= 'posts'
    

    
class DetailPostView(DetailView):
    template_name = 'detailpost.html'
    model = Post
    context_object_name = 'posts'
    
    
class CategoriesView(ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name= 'categories'
    
    
    
class CategoryView(DetailView):
    template_name = 'categorydetail.html'
    model = Category
    context_object_name = 'category' 
    
   
        
        
    