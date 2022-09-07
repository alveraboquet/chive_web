from django.db import models


# Create your models here.
class GPU(models.Model):

    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=10)
    price = models.IntegerField(blank=True)
    algo = models.CharField(max_length=10)
    hashrate = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    power = models.IntegerField(null=True)
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.model
