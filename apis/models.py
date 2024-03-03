from django.db import models

# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    name = models.CharField(max_length = 20, default="")
    email = models.CharField(max_length = 20, default="")
 
    def __str__(self):
        return self.title