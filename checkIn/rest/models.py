from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    givenname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class RawStudentData(models.Model):
    """
    Student data generated from https://www.mockaroo.com/
    """
    username = models.CharField(max_length=50, primary_key=True)
    givenname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    course1 = models.CharField(max_length=5, null=True)
    course2 = models.CharField(max_length=5, null=True)
    course3 = models.CharField(max_length=5, null=True)

