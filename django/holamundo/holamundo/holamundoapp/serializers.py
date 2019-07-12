from rest_framework import serializers 
from holamundo.holamundoapp.models import Computadora
#from proyecto.aplicacion.models import nombre_modelo

class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora 
        fields = '__all__'