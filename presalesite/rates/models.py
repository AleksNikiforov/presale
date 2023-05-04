from django.db import models



class Rates(models.Model):
    person = models.CharField(max_length=200)
    engineer_cost = models.FloatField(null=False)
    architect_cost = models.FloatField(null=False)
    manager_cost = models.FloatField(null=False)
    tech_writer_cost = models.FloatField(null=False)
    manager_coef = models.FloatField(null=False)
    tech_writer_coef = models.FloatField(null=False)

    def __str__(self):
        return self.person