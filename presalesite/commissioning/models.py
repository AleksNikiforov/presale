from django.db import models
from django.contrib.auth.models import User



class Commissioning(models.Model):
    name = models.CharField(max_length=200)
    days = models.FloatField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name
