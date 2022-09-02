from django.db import models

# Create your models here.
from django.db import models
class Parts(models.Model):
    id = models.AutoField
    pname= models.CharField(max_length=100)
    MRP =  models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    sold=models.IntegerField(default=0)
    place = models.CharField(max_length=100)
    def __str__(self):
        return  self.pname
#MRP,quantity,sold,place
class Service(models.Model):
    id = models.AutoField
    servicedate=models.DateField(auto_now=True)
    cname = models.CharField(max_length=70)
    bname = models.CharField(max_length=30)
    mobile = models.IntegerField(default=0)
    parts  = models.CharField(max_length=20000)
    rnumber= models.CharField(max_length=10)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return  self.cname
