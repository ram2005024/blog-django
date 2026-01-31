from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import About
# view for home base
def home(request):
   categories=Category.objects.all()
   featuredPosts=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
   posts=Blog.objects.filter(is_featured=False,status='Published').order_by('created_at')
   try:
      about=About.objects.get()
   except:
      about=None
   
   context={
      'categories':categories,
      'featuredPosts':featuredPosts,
      'posts':posts,
      'about':about
   }
   return render(request,'home.html',context)