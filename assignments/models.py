from django.db import models

#About model
class About(models.Model):
    about_description=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_description
    
# Social Media links
class SocialMedia(models.Model):
    social_platform=models.CharField(max_length=40)
    social_link=models.CharField(max_length=40,unique=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class  Meta:
        verbose_name_plural = 'Social links'

    def __str__(self):
        return self.social_platform