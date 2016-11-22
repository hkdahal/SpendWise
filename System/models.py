from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=100)


class Rent(models.Model):
    family = models.ForeignKey(Family)
    value = models.IntegerField()
    title = models.CharField(max_length=200)


class Grocery(models.Model):
    family = models.ForeignKey(Family)
    value = models.IntegerField()
    title = models.CharField(max_length=200)


class Car(models.Model):
    family = models.ForeignKey(Family)
    title = models.CharField(max_length=200)
    insurance = models.IntegerField()
    finance = models.IntegerField(default=0)



