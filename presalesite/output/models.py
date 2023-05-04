from django.db import models


class Output(models.Model):
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    summa_with_nds = models.FloatField(null=True)
    duration = models.FloatField(null=True)
    labor_cost_person = models.FloatField(null=True)
    labor_cost_mp = models.FloatField(null=True)
    labor_cost_rtd = models.FloatField(null=True)
    comment = models.CharField(max_length=200)

    
    # class Meta:
    #     ordering = ('name',)
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
