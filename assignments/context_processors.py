from .models import SocialMedia
#Context processor for Social Media links
def get_social_medias(request):
    social_links=SocialMedia.objects.all()
    return dict(social_links=social_links)