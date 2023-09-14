from django.db import models

# Create your models here.


class menu(models.Model):
    id = models.IntegerField(max_length=5, null=False, primary_key=True)
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField(max_length=5, null=False)

    def __str__(self):
        return self.title

# Create your models here.


class booking(models.Model):
    id = models.IntegerField(max_length=11, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    noofguests = models.IntegerField(max_length=6, null=False)
    bookingdate = models.DateField(null=False)

    def __str__(self):
        return self.name
