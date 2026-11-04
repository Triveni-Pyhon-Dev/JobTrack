
from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Interested', 'Interested'),
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )

    company_name = models.CharField(max_length=150)

    job_role = models.CharField(max_length=150)

    location = models.CharField(max_length=150)

    salary = models.CharField(max_length=100, blank=True)

    job_link = models.URLField(blank=True)

    job_description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Interested'
    )

    date_added = models.DateField(auto_now_add=True)

    applied_date = models.DateField(
        null=True,
        blank=True
    )

    interview_date = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"
