from django.db import models

# Create your models here.
class Hero(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    # nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=100) # habilidade mais poderosa
    poderes_secundarios = models.CharField(max_length=100) # habilidades de suporte

    jurisdicao = models.CharField(max_length=100) # cidade de atuação
    historia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codinome

# class seguindo(models.Model):
#     seguindo = models.ForeignKey(Hero, on_delete=models.CASCADE)
#     data = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"você esta seguindo{self.seguindo.codinome}"

# class seguidores(models.Model):
#     seguidores = models.ForeignKey(Hero, on_delete=models.CASCADE)
#     data = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.seguidores.codinome} esta seguindo você"
    


