from django import forms
from .models import Admission
class admission(forms.Form):
  id=forms.IntegerField()
  stu_name=forms.CharField()
  stu_father=forms.CharField()
  joindate=forms.DateField()
  stu_class=forms.CharField()
  fees=forms.IntegerField()
