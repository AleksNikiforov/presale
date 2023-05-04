from django.db import models



class Design(models.Model):
    name = models.CharField(max_length=200)
    days = models.FloatField(null=True)
    
    # class Meta:
    #     ordering = ('name',)
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name