
from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'job_role',
        'location',
        'status',
        'date_added',
        'user'
    )

    list_filter = ('status', 'date_added')

    search_fields = ('company_name', 'job_role')
