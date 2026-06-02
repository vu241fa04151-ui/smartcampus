from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'room_number',
        'title',
        'category',
        'priority',
        'status'
    )