from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from blogs.models import Category,Blog
from .forms import CategoryForm
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