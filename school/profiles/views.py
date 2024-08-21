from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def profiles(request):
  #return HttpResponse("<H1>Profiles</H1>")
   return render(request,'profiles.html',{})
