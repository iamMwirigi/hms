from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User # Assuming your custom user model is in 'users' app
# from hospital.models import Appointment, MedicalRecord # Import models as needed

def is_admin(user):
    """
    Checks if the user is authenticated and has the 'admin' role.
    """
    return user.is_authenticated and user.role == User.ROLE_CHOICES[0][0] # 'admin'

@login_required
@user_passes_test(is_admin)
def dashboard_home(request):
    # This is a placeholder. You'll fetch actual data for your dashboard.
    # Example: num_patients = PatientProfile.objects.count()
    data = {
        'message': f"Welcome to the Admin Dashboard API, {request.user.username if request.user.is_authenticated else 'Guest'}!",
        'info': "This endpoint will provide initial data for the React admin dashboard."
    }
    return JsonResponse(data)
