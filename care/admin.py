# care/admin.py
from django.contrib import admin
from .models import Infirmier, Patient

@admin.register(Infirmier)
class InfirmierAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department')
    search_fields = ('name', 'employee_id')
    list_filter = ('department',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'medical_record_id')
    search_fields = ('name', 'medical_record_id')
    list_filter = ('date_of_birth',)