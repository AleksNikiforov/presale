from django.db import models
from django.contrib.auth.models import User



class Other(models.Model):
    total_price = models.FloatField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    
    def __str__(self):
        return self.name
