from django.db import models
from django.utils.regex_helper import Choice

# Create your models here.



class Todo(models.Model):

    task = models.CharField(max_length=50)

    completed = models.BooleanField(null=True, default=False)

