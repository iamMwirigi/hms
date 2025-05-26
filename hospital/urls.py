from django.urls import path
from . import views # Import your views

# from . import views # You'll import views here later

app_name = 'hospital'  # Optional: good for namespacing URLs

urlpatterns = [
  path('', views.hospital_index, name='hospital_index'), 
    path('api/services/', views.list_services_api, name='api_list_services'), # New API URL
]
