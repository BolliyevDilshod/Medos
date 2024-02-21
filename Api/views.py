from django.shortcuts import render
from .serializer import SpecialistSerializers,HospitalsSerializers,PharmacysSerializers,SectionSerializers
from .models import Specialist,Hospitals,Pharmacys,Section
from rest_framework import generics




class SpecialistListView(generics.ListCreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializers

class SpecialistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SectionSerializers

class HospitalsListView(generics.ListCreateAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializers


class HospitalsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializers


class PharmacysListView(generics.ListCreateAPIView):
    queryset = Pharmacys.objects.all()
    serializer_class = PharmacysSerializers
    
class PharmacysDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacys.objects.all()
    serializer_class = PharmacysSerializers
    

class SectionView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SpecialistSerializers


class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SpecialistSerializers






