from django.db import models

# Create your models here.

class Stu(models.Model):
    image = models.ImageField(upload_to="pics")