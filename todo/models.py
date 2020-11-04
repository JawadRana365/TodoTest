from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    duedate=models.DateTimeField(default=timezone.now)
    priority=models.IntegerField(default=0)
    completed=models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class User(models.Model):
    userName=models.CharField(max_length=100)
    password=models.TextField()

    def __str__(self):
        return self.userName