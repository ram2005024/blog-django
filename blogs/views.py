from django.shortcuts import render
from .models import Blog,Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
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

# View for single blog handle
def single_blog(request,pId):
    single_blog=Blog.objects.get(slug=pId,status='Published')
    category=Category.objects.get(id=single_blog.category_id)
    
    return render(request,'single_blog.html',context={'single_blog':single_blog,'category':category})

# View for search blog
def search_blog(request):
    keyword=request.GET.get('keyword')
    # Fetch the blogs matching the keyword
    blogs=Blog.objects.filter(Q(title__icontains=keyword)|Q(short_body__icontains=keyword)|Q(short_description__icontains=keyword) ,status='Published')
    return render(request,'search_blogs.html',context={'posts':blogs,'keyword':keyword})
    