from django.db import models



class Examination(models.Model):
    name = models.CharField(max_length=200)
    days = models.FloatField(null=True)

    def __str__(self):
        return self.name
