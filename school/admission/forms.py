from django import forms

class admission(forms.Form):
  id=forms.IntegerField()
  stu_name=forms.CharField(max_length=255)
  stu_father=forms.CharField(max_length=255)
  joindate=forms.DateField()
  stu_class=forms.CharField()
  fees=forms.IntegerField()
