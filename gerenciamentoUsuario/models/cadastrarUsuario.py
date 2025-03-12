from django.db import models 
from .statusUsuario import *     

class CadastroUsuario(models.Model):
    
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.BigIntegerField(unique=True)
    senha = models.CharField(max_length=50)
    status = models.ForeignKey(StatusUsuario, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'CadastroUsuario'
        verbose_name = 'CadastroUsuario'
        verbose_name_plural = 'CadastroUsuarios'
        
    def __str__(self):
        return self.nome
    
    def __srt__(self):
        return self.status 
    
    