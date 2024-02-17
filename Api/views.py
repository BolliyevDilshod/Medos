from django.shortcuts import render
from .serializer import SpecialistSerializers,HospitalsSerializers,PharmacysSerializers
from .models import Specialist,Hospitals,Pharmacys,Section
from rest_framework import generics




class SpecialistListView(generics.ListCreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializers



class HospitalsListView(generics.ListCreateAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializers


class HospitalsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospitals.objects.all()
    serializer_class = HospitalsSerializers


class PharmacysListView(generics.ListCreateAPIView):
    queryset = Pharmacys.objects.all()
    serializer_class = PharmacysSerializers
    

class SectionView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SpecialistSerializers




