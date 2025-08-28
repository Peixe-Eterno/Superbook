from django.db import models
from heroes.models import Hero

# Create your models here.
class mensagens(models.Model):
    heroi = models.ForeignKey(Hero, on_delete=models.CASCADE)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
