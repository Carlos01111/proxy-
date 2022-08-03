from django.urls import path 
from bases import views
urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='detailpost'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('subcategory/<int:pk>/', views.SubcategoryView.as_view(), name='subcategory'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
