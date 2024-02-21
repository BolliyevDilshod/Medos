from django.urls import path
from .views import SpecialistListView,HospitalsListView,PharmacysListView,HospitalsDetailView,

urlpatterns = [
    path("<int:pk>/",HospitalsDetailView.as_view()),
    path('', SpecialistListView.as_view()),
    path('hospitals/', HospitalsListView.as_view()),
    path('pharmcy', PharmacysListView.as_view()),
    
]