from django.shortcuts import render
from django.http import HttpResponse
from admission.models import Admission
from admission.forms import admission
# Create your views here.

def home(request):
  students_data=Admission.objects.all()
  admission_form=admission()
  res=render(request,'index.html',{'students_data':students_data,'admission_form':admission_form})
  return res

def products(request):
  # return HttpResponse("<h1>Products Page</h1>")
  return render(request,'products.html',{})

def services(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'services.html',{})
def login(request):
   #return HttpResponse("<h1>Login</h1>")
	 return render(request,'login.html',{})
  