from django.db import models
class Courses(models.Model):
        nome = models.CharField(max_length=100)
        description = models.TextField(max_length=500)
        img = models.CharField(max_length=100)

