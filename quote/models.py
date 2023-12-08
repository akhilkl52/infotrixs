from django.db import models

# Create your models here.

class Quote(models.Model):
    auther = models.CharField(max_length=50)
    text = models.TextField()


    def __str__(self) :
        return self.auther