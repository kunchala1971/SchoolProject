from django.shortcuts import redirect, render
from django.http import HttpResponse
from admission.models import Admission
from admission.forms import admission
# Create your views here.

def home(request):
  students_data=Admission.objects.all()
  res=render(request,'index.html',{'students_data':students_data})
  return res

def admissionentry(request):
  # admission_form=admission()
  if request.method=='POST':
    result=admission(request.POST)
    if result.is_valid():
      id=result.cleaned_data['id']
      stu_name=result.cleaned_data['stu_name']
      stu_father=result.cleaned_data['stu_father']
      joindate=result.cleaned_data['joindate']
      stu_class=result.cleaned_data['stu_class']
      fees=result.cleaned_data['fees']
      fs=open("students.txt",'a')
      fs.write("\n-------------------------------------")
      fs.write("\nID							: " + str(id))
      fs.write("\nName						: " + str(stu_name))
      fs.write("\nFather					: " + str(stu_father))
      fs.write("\nJoinDate				: " + str(joindate))
      fs.write("\nCourse					: " + str(stu_class))
      fs.write("\nFees						: " + str(fees))
      fs.close 
      return redirect('home')
      
  res=render(request,'admissionentry.html',{})
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
  