
import json

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import JobApplication
from .forms import JobApplicationForm, RegistrationForm


@login_required
def dashboard(request):
    jobs = JobApplication.objects.filter(user=request.user)

    statuses = [
        'Interested',
        'Applied',
        'Interview',
        'Selected',
        'Rejected',
    ]

    status_counts = {
        status: jobs.filter(status=status).count()
        for status in statuses
    }

    total_jobs = jobs.count()

    monthly_data = (
        jobs.annotate(month=TruncMonth('date_added'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    month_labels = [
        item['month'].strftime('%b %Y')
        for item in monthly_data
    ]

    month_values = [
        item['total']
        for item in monthly_data
    ]

    search = request.GET.get('search', '')
    selected_status = request.GET.get('status', '')

    if search:
        jobs = jobs.filter(
            Q(company_name__icontains=search) |
            Q(job_role__icontains=search)
        )

    if selected_status in statuses:
        jobs = jobs.filter(status=selected_status)

    jobs = jobs.order_by('-date_added')

    context = {
        'jobs': jobs,
        'total_jobs': total_jobs,
        'applied_count': status_counts['Applied'],
        'interview_count': status_counts['Interview'],
        'selected_count': status_counts['Selected'],
        'status_labels': json.dumps(statuses),
        'status_values': json.dumps([
            status_counts[status] for status in statuses
        ]),
        'month_labels': json.dumps(month_labels),
        'month_values': json.dumps(month_values),
        'search': search,
        'selected_status': selected_status,
    }

    return render(request, 'jobs/dashboard.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()

            messages.success(request, 'Job saved successfully!')
            return redirect('dashboard')
    else:
        form = JobApplicationForm()

    return render(
        request,
        'jobs/job_form.html',
        {'form': form, 'page_title': 'Add New Job'}
    )


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('dashboard')
    else:
        form = JobApplicationForm(instance=job)

    return render(
        request,
        'jobs/job_form.html',
        {'form': form, 'page_title': 'Edit Job'}
    )


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(
        JobApplication,
        id=job_id,
        user=request.user
    )

    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')

    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
