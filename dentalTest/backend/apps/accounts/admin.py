from django.contrib import admin
from .models import User
from .models import Doctor
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'last_name',
        'avatar',
        'phone',
        'age',
    ]

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'last_name',
        'avatar',
        'phone',
        'special_key',
        'is_active',
        'is_superuser'
    ]


