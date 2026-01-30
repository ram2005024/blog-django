from django.shortcuts import render
from .models import Blog,Category
from django.shortcuts import get_object_or_404
# Create your views here.
# View to get all the category posts 
def get_category_posts(request,id):
    category=get_object_or_404(Category,id=id)
    posts=Blog.objects.filter(category_id=id)
    context={
        'posts':posts,
        'category':category
        
    }
    return render(request,'get_category_posts.html',context)
