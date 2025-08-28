from django.db import models

# Create your models here.
class Conta(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)