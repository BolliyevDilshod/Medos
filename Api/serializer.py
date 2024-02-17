from rest_framework import serializers
from .models import Specialist,Hospitals,Pharmacys,Section

class SpecialistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'


class HospitalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = '__all__'


class PharmacysSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pharmacys
        fields = '__all__'

class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        
        
        

