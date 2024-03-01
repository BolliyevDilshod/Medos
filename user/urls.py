from django.urls import path
from .views import DoctorRegistration, HospitalRegistration, AdminRegistration, CustomAuthToken,DoctorProfile,HospitalProfile,CategoryView
from rest_framework.routers import DefaultRouter

register_router = DefaultRouter()
user_router = DefaultRouter()

register_router.register(r'doctor',DoctorRegistration,basename='doctor-register')
register_router.register(r'hospital',HospitalRegistration,basename='hospital-register')
register_router.register(r'admin',AdminRegistration,basename='admin-register')
register_router.register(r'login',CustomAuthToken,basename='login')
user_router.register(r'doctor-profile',DoctorProfile,basename='doctor-profile')
user_router.register(r'hospital-profile',HospitalProfile,basename='hospital-profile')
user_router.register(r'category',CategoryView,basename='category')
