from django.db import models

# Create your models here.
class Profile(models.Model):
  stu_name = models.CharField(max_length=100)
  stu_code=models.IntegerField()

  class Meta:
    verbose_name="Profile"
    verbose_name_plural="Profiles"
