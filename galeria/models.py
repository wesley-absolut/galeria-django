from django.db import models


class Categoria (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Imagem(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.ImageField(upload_to='galeria/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='imagens')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
