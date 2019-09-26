from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publisher = models.CharField(max_length=400)
    release_date = models.DateField()


class Author(models.Model):
    name = models.CharField(max_length=225)
    biography  = models.TextField()
    date_of_birth = models.DateField()
    