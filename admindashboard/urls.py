from django.urls import path
from . import views

app_name = 'admindashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    # Add other dashboard-specific URLs here
]