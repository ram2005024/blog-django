from django.urls import path
from . import views
urlpatterns = [
    path('category/<int:id>',views.get_category_posts,name='get_category_posts')
]
