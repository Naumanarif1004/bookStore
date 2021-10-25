import uuid

# Django
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Book(models.Model):
    writer = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    synopsis = models.TextField(null=True,blank=True)
    genre = models.CharField(max_length=100,null=True,blank=True)
    release_date = models.DateField(auto_now=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)