from django.db import models

# Create your models here.
class Book(models.Model):
    cover_page = models.ImageField()
    title = models.CharField(max_length=50)
    book = models.FileField()

    def get_n_pages(n):
        pass