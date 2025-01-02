from django.db import models

# Create your models here.
class Slides(models.Model):
    title=models.CharField(max_length=50)
    deccription=models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='static/images/', default="")
