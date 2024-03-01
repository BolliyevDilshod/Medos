from rest_framework.response import Response
from .serializers import DoctorSerializer, HospitalSerializer, AdminSerializer,DoctorProfileSerializer,HospitalProfileSeriazer,CategorySerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import Doctor,Hospital,Admin,Category
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .permissions import IsAdmin,IsDoctor,IsHospital
from rest_framework import status
from rest_framework.decorators import action

class CustomAuthToken(ViewSet):
    
    def create(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class DoctorRegistration(ModelViewSet):
    serializer_class = DoctorSerializer
    http_method_names = ['post']

class HospitalRegistration(ModelViewSet):
    serializer_class = HospitalSerializer
    http_method_names = ['post']

class AdminRegistration(ModelViewSet):
    serializer_class = AdminSerializer
    http_method_names = ['post']

class DoctorProfile(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorProfileSerializer
    http_method_names = ['get','patch']
    permission_classes = (IsAuthenticated,IsDoctor)

    def list(self, request, *args, **kwargs):
        serializer = DoctorProfileSerializer(request.user.doctor)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HospitalProfile(ModelViewSet):    
    queryset = Hospital.objects.all()
    serializer_class = HospitalProfileSeriazer
    http_method_names = ['get','patch']
    permission_classes = (IsAuthenticated,IsHospital)

    def list(self, request, *args, **kwargs):
        serializer = HospitalProfileSeriazer(request.user.hospital)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CategoryView(ViewSet):

    def list(self,request):
        categroies = Category.objects.all()
        serializer = CategorySerializer(categroies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    @action(detail=False, methods=['get'])
    def with_hospal(self, request, *args, **kwargs):
        categroies = Category.filter.get_categories_with_count_hospitals()
        serializer = CategorySerializer(categroies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def with_doctor(self, request, *args, **kwargs):
        categroies = Category.filter.get_categories_with_count_doctors()
        serializer = CategorySerializer(categroies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
