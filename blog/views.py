from django.shortcuts import render
from django.http import HttpResponse
# view for home base
def home(request):
   return render(request,'home.html')