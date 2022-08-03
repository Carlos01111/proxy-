from multiprocessing import context
from typing import List
from unicodedata import category
from django.shortcuts import render
#vistas genericas
from django.views.generic import ListView, DetailView, TemplateView

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
    
    
    
class CategoryView(TemplateView):
    template_name = 'category.html'
    
    def get_context_data(self,**kwargs):
        context=  super().get_context_data(**kwargs)
        category_id = self.kwargs['pk']
        context['category'] = Category.objects.get(id=category_id)
        # context['subcategories'] = Subcategory.objects.filter(pk=category_id)
        return context
        

class SubcategoryView(TemplateView):
    # template_name = 'subcategory.html'
    # model = Subcategory
    # context_object_name = 'subcategory' 
    template_name = 'subcategory.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory_id = self.kwargs['pk']
        context['subcategory'] = Subcategory.objects.get(id=subcategory_id)
        
        return context