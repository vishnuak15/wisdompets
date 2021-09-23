from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=200)
    submitter = models.CharField(max_length=200)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.name
class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name