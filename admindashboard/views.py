from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
# from users.models import User # Assuming your custom user model is in 'users' app
# from hospital.models import Doctor, Patient, Appointment # Import other models as needed

# def is_admin(user):
#     # Implement your logic to check if the user is an admin
#     # Example: return user.is_authenticated and user.role == User.ROLE_ADMIN
#     # Or: return user.is_authenticated and user.is_staff
#     return user.is_authenticated and user.is_staff # A common check

# @login_required
# @user_passes_test(is_admin)
def dashboard_home(request):
    # This is a placeholder. You'll fetch actual data for your dashboard.
    data = {
        'message': f"Welcome to the Admin Dashboard API, {request.user.username if request.user.is_authenticated else 'Guest'}!",
        'info': "This endpoint will provide initial data for the React admin dashboard."
    }
    return JsonResponse(data)
