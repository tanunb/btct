# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Price(models.Model):
    current_price = models.CharField(max_length=100)
    currency = models.CharField(max_length=30)
    time = models.DateField()

class Article(models.Model):
    topic = models.CharField(max_length=500)
    date = models.DateField()
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.topic + ':' + self.content