from django.urls import path
from . import views

urlpatterns = [
     path("",views.dashboard,name="dashboard"),
    #  Categories endpoint
     path("categories",views.categories,name="categories_dashboard"),
     path("categories/add",views.add_new_category,name="add_new_category"),
     path("categories/edit/<int:id>",views.edit_category,name='edit_category'),
     path("categories/delete/<int:id>",views.delete_category,name='delete_category'),
    #  Posts endpoints
     path("posts",views.posts,name="posts"),
     path("posts/add",views.add_posts,name='add_posts')
 ]
 