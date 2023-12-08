from django.db import models

# Create your models here.
class Avtomobile(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True, default=2000)
    color = models.CharField(max_length=30, null=True, blank=True, default='black')
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


