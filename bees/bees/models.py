from django.db import models

# Create your models here.
class Bee(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title