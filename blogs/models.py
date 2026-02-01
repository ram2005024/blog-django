from django.db import models
from django.contrib.auth.models import User
# Cateogries model
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='categories'
    def __str__(self):
        return self.category_name

#Blog model
STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published")
)
class Blog(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
    is_featured=models.BooleanField(default=False)
    short_description=models.TextField(max_length=500)
    short_body=models.TextField(max_length=2000)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment