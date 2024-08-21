from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  # return HttpResponse("<H1>Hello Sample View</H1>")
   return render(request,'index.html',{})

def products(request):
  # return HttpResponse("<h1>Products Page</h1>")
  return render(request,'products.html',{})

def services(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'services.html',{})
def login(request):
   #return HttpResponse("<h1>Login</h1>")
	 return render(request,'login.html',{})