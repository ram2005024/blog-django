from django.contrib import admin
from .models import Blog,Category,Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={
        "slug":("title",)
    }
    list_display=(
        'title',
        'author',
        'is_featured',
        'status'
    )
    search_fields=(
      'id',
      'title',
      'category__category_name',
      'status'
        
    )
    list_editable=('is_featured',)
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)