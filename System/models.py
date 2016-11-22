from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Rent(models.Model):
    family = models.ForeignKey(Family)
    value = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return 'Rent; ' + self.title + ' for ' + self.family


class Grocery(models.Model):
    family = models.ForeignKey(Family)
    value = models.IntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return 'Grocery: ' + self.title + ' for ' + self.family


class Car(models.Model):
    family = models.ForeignKey(Family)
    title = models.CharField(max_length=200)
    insurance = models.IntegerField()
    finance = models.IntegerField(default=0)

    def __str__(self):
        return 'Car:' + self.title + ' for ' + self.family



