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
     path("posts/add",views.add_posts,name='add_posts'),
     path("posts/edit/<int:id>",views.edit_posts,name='edit_posts'),
     path("posts/delete/<int:id>",views.delete_posts,name='delete_posts'),

    #  Users endpoints
    path('users',views.users,name="users"),
    path('users/add_user',views.add_users,name='add_user'),
    path('users/edit_user/<int:id>',views.edit_users,name='edit_user'),
    path('users/delete_user/<int:id>',views.delete_users,name='delete_user')
 ]
 