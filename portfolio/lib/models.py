
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

"""
This models.py file is given to Saroj Mishra for some assignment.
This is a model designed for the library management app's database, it contains four model classes as given below
study carefully the model classes and their field, how are they related to each other and more.
"""

# Create your models here.

class Member(models.Model):
    """This model contains the detail about the members of the library who can issue book from the library."""
    name=models.CharField(max_length=100)
    rollnumber=models.CharField(max_length=50,unique=True)
    uniqueCode=models.CharField(max_length=50,blank=True,default='')

class Book(models.Model):
    """This model contains all the details about the unique books availale in the library"""
    name=models.CharField(max_length=100)
    remaining=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    author=models.CharField(max_length=500)

class BooksDetail(models.Model):
    """This model stores the information about the copies of the same book available in the Library."""
    code=models.CharField(max_length=50,unique=True)
    book=models.ForeignKey(Book, related_name='tracks', on_delete=models.CASCADE)
    isIssued=models.BooleanField(default=False)

class IssueDetail(models.Model):
    """This model contains the detail about the transaction i.e the detail like when a student issued a book and when did he return it"""
    member=models.ForeignKey(Member, related_name='tracks', on_delete=models.CASCADE)
    books_detail=models.ForeignKey(BooksDetail)
    issue_date=models.DateTimeField()
    return_date=models.DateTimeField(blank=True,null=True)

class ReturnDate(models.Model):
    """This model is for some other propose you don't need to bother now"""
    returnDate=models.DateTimeField()
    gThan=models.IntegerField(default=0)
    lThan=models.IntegerField(default=1000000000)



# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

