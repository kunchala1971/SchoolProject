from django.db import models

# Create your models here.
class TransportDetail(models.Model):
  stu_name = models.CharField(max_length=100)
  route = models.CharField(max_length=100)
  fees = models.PositiveIntegerField()

  class Meta:
    verbose_name="TransportDetail"
    verbose_name_plural="TransportDetails"
  
class RouteDetail(models.Model):
  route_name = models.CharField(max_length=100)
  distance =  models.PositiveIntegerField()
  price = models.PositiveIntegerField()

  class Meta:
    verbose_name="RouteDetail"
    verbose_name_plural="RouteDetails"