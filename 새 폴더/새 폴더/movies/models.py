from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=500)
    overview = models.TextField()
        
    def __str__(self):
        return self.title