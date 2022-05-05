from django.db import models
import string  # for string constants
import random  # for generating random strings


class PageContents(models.Model):
    page_name = models.CharField(max_length=200, primary_key=True)
    owners = models.TextField(null=True)
    status = models.TextField(null=True)


class Documents(models.Model):
    title = models.CharField(max_length=200)
    page_name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    file = models.FileField(upload_to='uploads/')
