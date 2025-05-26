from django.http import HttpResponse, JsonResponse


def hospital_index(request):
    return HttpResponse("Welcome to the Hospital section!")

def list_services_api(request):
    # In a real app, you'd fetch this from a Service model
    # or some other data source.
    services_data = [
        {"id": 1, "name": "General Consultation", "department": "Outpatient"},
        {"id": 2, "name": "Cardiology Check-up", "department": "Cardiology"},
        {"id": 3, "name": "X-Ray", "department": "Radiology"},
    ]
    return JsonResponse(services_data, safe=False) # safe=False for list responses
