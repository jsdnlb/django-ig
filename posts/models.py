"""Posts Models"""

from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

"""Important documentation and references"""
# Doc models fields references: https://docs.djangoproject.com/en/2.0/ref/models/fields/
# Setting django datebases: https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# Making querys: https://docs.djangoproject.com/en/2.0/topics/db/queries/


# Commands
# python3 manage.py makemigrations Search the new changes in ours models and it will reflect then in a folder migrations
# python3 manage.py It will apply change in our database


# Create your models here.
class User(models.Model):
    """User models"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    # More characters
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)
    # auto_now_add Put Date when create 
    # auto_now Modi
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # By default it returns an object, this changes it to return the email address.
    def __str__(self) -> str:
        """Return Email"""
        return self.email