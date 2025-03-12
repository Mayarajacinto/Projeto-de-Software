from rest_framework import serializers
from ..models import cadastrarUsuario, StatusUsuario

class StatusUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusUsuario
        fields = [
            'status'
        ]
        
class CadastrarUsuarioSerializer(serializers.ModelSerializer):
    statusUsuario = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarUsuario
        fields = [
            'nome',
            'email',
            'senha',
            'statusUsuario'
            'cpf'
            'status'
        ]
        
    def get_statusUsuario(self, obj):
        return obj.statusUsuario.status
    
    def get_cadastrarUsuario(self, obj):
        return obj.cadastrarUsuario.nome
    
    def get_cadastrarUsuario(self, obj):
        return obj.cadastrarUsuario.cpf