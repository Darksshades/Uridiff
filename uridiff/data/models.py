from django.db import models

class Question(models.Model):

    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    solved = models.CharField(max_length=10, blank=True)
    level = models.IntegerField(default=1)
