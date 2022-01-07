"""Posts Models"""

from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
# Doc models fields references: https://docs.djangoproject.com/en/2.0/ref/models/fields/
# Setting django datebases: https://docs.djangoproject.com/en/2.0/ref/settings/#databases


# Commands
# python3 manage.py makemigrations Search the new changes in ours models and it will reflect then in a folder migrations
# python3 manage.py It will apply change in our database

class User(models.Model):
    """User models"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # More characters
    bio = models.TextField(blank=True)

    birthday = models.DateField(blank=True, null=True)
    # auto_now_add Put Date when create 
    # auto_now Modi
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)