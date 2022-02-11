from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    prod=products.objects.all()
    ct=categ.objects.all()
    return render(request,"home.html",{'pr':prod,'ct':ct})
