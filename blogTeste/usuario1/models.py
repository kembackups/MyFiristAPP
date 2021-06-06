from django.db import models
from django.db.models.base import Model

# USUARIO 1
# nomes
class Nome(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    def __str__(self):
        return self.nome
# Telefones
class Telefone(models.Model):
    telefone = models.CharField(
        max_length=11,
        verbose_name='Celular'
    )    
    def __str__(self):
        return (self.telefone)

# Endereços
class Endereco(models.Model):
    endereco = models.CharField(
        max_length=50
    )
    
    def __str__(self):
        return self.endereco
    
    class Meta:
        verbose_name_plural = 'Endereços'    

# Email
class Email(models.Model):
    email = models.EmailField(
        max_length=100,
        default='exemplo@exemplo'
    )
    
    def __str__(self):
        return (self.email)
    
    class Meta:
        verbose_name_plural = 'E-mail'    