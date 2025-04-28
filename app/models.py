from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class HomePage(models.Model):
    header_image = models.ImageField()
    htmlContent = HTMLField()

class Reviews(models.Model):
    page = models.ForeignKey(HomePage,on_delete=models.CASCADE,related_name='reviews')
    image = models.ImageField()