from distutils.command.upload import upload
from django.db import models

# Create your models here.

class ModelClass(models.Model):
    create_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(ModelClass):
    name = models.CharField(max_length=100, unique=True, help_text='name')
    description = models.CharField(max_length=300, help_text='description')
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Subcategory(ModelClass):
    name = models.CharField(max_length=100, help_text='name')
    description = models.CharField(max_length=300, help_text='description')
    image = models.ImageField(upload_to='subcategory', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

class Author(ModelClass):
    name = models.CharField(max_length=100, help_text='name')
    image = models.ImageField(upload_to='author')
    surname = models.CharField(max_length=100, help_text='surname')
    email = models.EmailField(help_text='email')
    phone = models.CharField(help_text='phone', max_length=100)
    website = models.URLField(help_text='website')
    description = models.CharField(max_length=300, help_text=300, blank=True, null=True)
    social_network = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Post(ModelClass):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='title')
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class PostContent(ModelClass):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    subtitle =  models.CharField(max_length=100, help_text='subtitle')
    step = models.IntegerField(blank=True, null=True)
    imagecontent = models.ImageField(upload_to='posts/imagecontent/')
    content = models.TextField(help_text='content')

    def __str__(self):
        return self.subtitle

    class Meta:
        verbose_name='content'
        verbose_name_plural = 'contents'
