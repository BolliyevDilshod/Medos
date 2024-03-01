from django.contrib import admin

# Register your models here.
from .models import Admin,Doctor,Hospital,CustomUser,Category

admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(CustomUser)
admin.site.register(Category)