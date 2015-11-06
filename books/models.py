# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.
class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Country = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Name
class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=10)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=30)
    PublishDate = models.DateField()
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return self.Title