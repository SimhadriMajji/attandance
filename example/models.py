from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
  username=models.CharField(max_length=100,primary_key=True)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)
  def _str_(self):
    return self.username

class Teacher(models.Model):
  username=models.CharField(max_length=100,primary_key=True)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)
  def _str_(self):
    return self.username
