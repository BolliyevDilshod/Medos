# models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager,DoctorManager,HospitalManager,AdminManager,CategoryManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class WorkingDays(models.Model):
    day = models.CharField(max_length = 30)

    def __str__(self):
        return self.day

class Category(models.Model):
    name = models.CharField(max_length = 100)

    objects = models.Manager()
    filter = CategoryManager()

    def __str__(self) -> str:
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):

    class UserType(models.TextChoices):
        ADMIN = 'Admin'
        DOCTOR = 'Doctor'
        HOSPITAL = 'Hospital'

    user_type = models.CharField(max_length = 8,choices = UserType.choices, default = UserType.ADMIN)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'),blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


    def is_admin(self):
        admin_role = str(self.UserType.ADMIN)
        return self.user_type == admin_role

    def is_doctor(self):
        doctor_role = str(self.UserType.DOCTOR)
        return self.user_type == doctor_role

    def is_hospital(self):
        hospital_role = str(self.UserType.HOSPITAL)
        return self.user_type == hospital_role

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Doctor(CustomUser):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    middle_name = models.CharField(max_length = 30,blank=True,null=True)
    image = models.FileField(upload_to='Doctor/',blank=True,null=True)
    experience = models.PositiveIntegerField(blank=True,null=True)
    phone = models.CharField(max_length = 20,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    working_days = models.ManyToManyField(WorkingDays,blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    consultation_fee = models.FloatField(blank=True, null=True)
    specialty = models.ManyToManyField(Category,blank=True)
    address = models.TextField(blank=True, null=True)

    location = models.CharField(max_length = 50, blank=True, null=True)

    view = models.PositiveIntegerField(blank =True, default = 0)
    like = models.PositiveIntegerField(blank =True, default = 0)

    objects = DoctorManager()

    class Meta:
        verbose_name = _('doctor')
        verbose_name_plural = _('doctors')

class Hospital(CustomUser):
    name = models.CharField(max_length = 50)
    image = models.FileField(upload_to='Hospital/',blank=True,null=True)
    phone = models.CharField(max_length = 20,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    working_days = models.ManyToManyField(WorkingDays,blank=True)
    specialty = models.ManyToManyField(Category,blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    location = models.CharField(max_length = 50, blank=True, null=True)

    view = models.PositiveIntegerField(blank =True, default = 0)
    like = models.PositiveIntegerField(blank =True, default = 0)
    objects = HospitalManager()
    class Meta:
        verbose_name = _('hospital')
        verbose_name_plural = _('hospitals')

class Admin(CustomUser):
    objects = AdminManager()
    class Meta:
        verbose_name = _('admin')
        verbose_name_plural = _('admins')
