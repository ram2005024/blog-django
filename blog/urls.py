from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from blogs import views as BlogView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('blogs/',include('blogs.urls')),
    # search blog
    path('blogs/search/',BlogView.search_blog,name='search_blog'),
    path('blogs/<slug:pId>',BlogView.single_blog,name="single_blog"),
    path("register",views.register,name='register'),
    path("login",views.user_login,name="login"),
    path("logout",views.user_logout,name="logout"),
    path("dashboard",include('dashboard.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
