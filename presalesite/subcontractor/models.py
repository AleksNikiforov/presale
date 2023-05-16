from django.db import models
from django.contrib.auth.models import User



class Subcontractor(models.Model):
    subcontract_name = models.CharField(max_length=200)
    subcontract_jobs = models.CharField(max_length=200)
    subcontract_price = models.FloatField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    
    def __str__(self):
        return self.name
