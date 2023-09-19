from django.db import models

# Create your models here.

class Data(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.TextField()
    category = models.CharField(max_length=50)
    start_date = models.DateField()
    importance = models.CharField(max_length=50)
