# serializers.py
from rest_framework import serializers
from .models import Doctor, Hospital, Admin, Category


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['username', 'password','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            }

    def create(self, validated_data):
        validated_data['user_type'] = 'Doctor'
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['username', 'password', 'name']
        extra_kwargs = {
            'password': {'write_only': True},
            }

    def create(self, validated_data):
        validated_data['user_type'] = 'Hospital'
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
    
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ['password','last_login','is_active','is_staff','is_superuser','date_joined','groups','user_permissions']
        extra_kwargs = {
            'view': {'read_only': True},
            'like': {'read_only': True},
            }

class HospitalProfileSeriazer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        exclude = ['password','last_login','is_active','is_staff','is_superuser','date_joined','groups','user_permissions']
        extra_kwargs = {
            'view': {'read_only': True},
            'like': {'read_only': True},
            }

class CategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only = True)

    class Meta:
        model = Category
        fields = ['name','count']
