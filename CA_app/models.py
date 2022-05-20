from django.db import models
from phone_field import PhoneField

# Create your models here.


class candidate(models.Model):
    Firstname = models.CharField(max_length=50, null=True)
    Lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname


class Contact(models.Model):
    Your_Name = models.CharField(max_length=200)
    Your_Email = models.EmailField(max_length=100)
    Your_Subject = models.CharField(max_length=200)
    Your_Message = models.TextField()

    def __str__(self):
        return self.Your_Name


class Headline(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Request_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=100)

    def __str__(self):
        return self.name
