from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def transport(request):
  #return HttpResponse("<H1>Trasport</H1>")
 	return render(request,'transport.html',{})
