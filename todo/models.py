from django.db import models

# Create your models here.

class Task(models.Model):
  id=models.AutoField(primary_key=True)
  item=models.CharField(max_length=30)