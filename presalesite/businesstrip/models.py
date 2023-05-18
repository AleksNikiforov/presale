from django.db import models
from django.contrib.auth.models import User


class BusinessTrip(models.Model):
    duration_trip = models.FloatField(null=False)
    ticket_cost = models.FloatField(null=False)
    hotel_cost = models.FloatField(null=False)
    daily_allowance = models.FloatField(null=False)
    total_cost = models.FloatField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.person