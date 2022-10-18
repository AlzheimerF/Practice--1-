from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Goods(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    branch = models.ForeignKey('Shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

