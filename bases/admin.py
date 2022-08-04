from django.contrib import admin
from bases.models import Category, Subcategory, Author, Post, PostContent, File
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostContent)
admin.site.register(File)
