
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import EmailAuthenticationForm


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('add/', views.add_job, name='add_job'),
    path('edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete/<int:job_id>/', views.delete_job, name='delete_job'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=EmailAuthenticationForm
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('register/', views.register, name='register'),
]
