from django.urls import path 
from bases import views
urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='detailpost'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    
]
