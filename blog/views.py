from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About
from django.contrib import messages
from django.contrib.auth import login,logout
from .forms import RegisterForm,LoginForm
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

#View for register
def register(request):

   if request.method=='POST':
      form=RegisterForm(request.POST)
      if(form.is_valid()):
         form.save()
         return redirect('home')
      else:
         return render(request,'register.html',context={'form':form})
   form=RegisterForm()
   return render(request,'register.html',context={'form':form})

# View for login
def user_login(request):
   if request.method=='POST':
      form=LoginForm(request,request.POST)
      if form.is_valid():
         user=form.get_user()
         login(request,user)
         return redirect('dashboard')
      else:
         return render(request,'login.html',context={'form':form})
   form=LoginForm()
   return render(request,'login.html',context={'form':form})
   
# Views for user logout
def user_logout(request):
   logout(request)
   return redirect('home')