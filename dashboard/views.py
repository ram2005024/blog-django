from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from blogs.models import Category,Blog
from .forms import CategoryForm,PostForm,UserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.
# Dashboard view
@login_required(login_url='login')
def dashboard(request):
  categoriesNo=Category.objects.all().count()
  postsNo=Blog.objects.filter(status='Published').count()
  return  render(request,'dashboard/dashboard.html',context={
    'catCount':categoriesNo,
    'postCount':postsNo
  })
# Categories dashboard view

def categories(request):
  return render(request,'dashboard/categories.html')

#Add new category in dashboard
def add_new_category(request):
  if request.method=='POST':
    form=CategoryForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('categories_dashboard')
  else:
     form=CategoryForm()
     return render(request,'dashboard/addCategories.html',context={'form':form})
   
# Edit the category from a dashboard section
def edit_category(request,id):
  category=Category.objects.get(id=id)
  if request.method=='POST':
     form=CategoryForm(request.POST,instance=category)
     if form.is_valid():
        form.save()
        return redirect('categories_dashboard')
     else:
        return render(request,'dashboard/categories.html')
  else:
     form=CategoryForm(instance=category)
     return render(request,'dashboard/edit_category.html',{'form':form})
  
  # View to delete the dashboard category
def delete_category(request,id):
  
  category=get_object_or_404(Category,id=id)
  category.delete()
  return redirect('categories_dashboard')
# For dashoboard posts
def posts(request):
   posts=Blog.objects.all()
   context={
      'posts':posts
   }
   return render(request,'dashboard/dashboard_posts.html',context)
def add_posts(request):
  if request.method=='POST':
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
          post=form.save(commit=False)
          post.author=request.user
          post.save()
          title=form.cleaned_data['title']
          post.slug=slugify(title) + '-' + str(post.id)
          post.save()
          return redirect("posts")
    else:
         
         return render(request,"dashboard/add_posts.html",context={
            'form':form
         })
  else:
    form=PostForm()
    return render(request,'dashboard/add_posts.html',context={
       'form':form
    })
def edit_posts(request,id):
  post=get_object_or_404(Blog,id=id)
  if request.method=='POST':
    form=PostForm(request.POST,request.FILES,instance=post)
    if form.is_valid():
      post=form.save(commit=False)
      post.author=request.user
      post.save()
      title=form.cleaned_data['title']
      post.slug=slugify(title) + '-' + str(post.id)
      post.save()
      return redirect("posts")
    else:
         
         return render(request,"dashboard/edit_posts.html",context={
            'form':form
         })
  else:
    form=PostForm(instance=post)
    return render(request,'dashboard/edit_posts.html',context={
       'form':form
    })
def delete_posts(request,id):
   post=get_object_or_404(Blog,id=id)
   post.delete()
   return redirect('posts')

# For user views
@permission_required('auth.view_user',raise_exception=True)
def users(request):
   users=User.objects.all()
   return render(request,'dashboard/view_users.html',context={'users':users})
@permission_required('auth.view_user',raise_exception=True)
def add_users(request):
  if request.method=='POST':
    form=UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users')
    else:
      return render(request,'dashboard/add_users.html',context={'form':form})
  else: 
        form=UserForm()
        return render(request,'dashboard/add_users.html',context={'form':form})
@permission_required('auth.view_user',raise_exception=True)
def edit_users(request,id):
  user=get_object_or_404(User,id=id)
  form=EditUserForm(instance=user)
  if request.method=='POST':
    form=EditUserForm(request.POST,instance=user)
    if form.is_valid():
      form.save()
      return redirect('users')
    else:
      return render(request,'dashboard/user_edit.html',context={'form':form})
  else:
    return render(request,'dashboard/user_edit.html',context={'form':form})
@permission_required('auth.view_user',raise_exception=True)
def delete_users(request,id):
   user=get_object_or_404(User,id=id)
   user.delete()
   return redirect('users')
