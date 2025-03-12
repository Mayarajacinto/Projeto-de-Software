from rest_framework import serializers
from ..models import Evento, StatusServico

class StatusServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusServico
        fields = [
            'statusEvento'
        ]
        
class EventoSerializer(serializers.ModelSerializer):
    statusServico = serializers.SerializerMethodField()
    
    class Meta:
        model = Evento
        fields = [
            'nome',
            'data',
            'horario',
            'local',
            'statusServico'
        ]
        
    def get_statusServico(self, obj):
        return obj.statusServico.statusEvento
    
    def get_evento(self, obj):
        return obj.servico.nome 
    
    def get_data(self, obj):
        return obj.servico.data
    
    def get_horario(self, obj):
        return obj.servico.horario
    
    def get_local(self, obj):
        return obj.servico.local
    
    