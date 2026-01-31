from django.contrib import admin
from .models import About,SocialMedia
# Register your models here.

class AboutModel(admin.ModelAdmin):
    def has_add_permission(self, request):
       if About.objects.exists():
           return False
       return True

admin.site.register(About,AboutModel)
admin.site.register(SocialMedia)