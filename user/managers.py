from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Count


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        if not password:
            raise ValueError("The given password must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)

class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='Admin')

class DoctorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='Doctor')

class HospitalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='Hospital')

class CategoryManager(models.Manager):
    
    def get_categories_with_count_hospitals(self):
        return self.annotate(count=Count('hospital'))
    
    def get_categories_with_count_doctors(self):
        return self.annotate(count=Count('doctor'))
