from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer
from .forms import WheelSpecificationForm

# ✅ API View: POST - Create new wheel specification
class WheelSpecificationCreateView(generics.CreateAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": data.get("formNumber"),
                "submittedBy": data.get("submittedBy"),
                "submittedDate": data.get("submittedDate"),
                "status": "Saved"
            }
        }, status=status.HTTP_201_CREATED)

# ✅ API View: GET - Fetch filtered wheel specifications
class WheelSpecificationListView(APIView):
    def get(self, request):
        queryset = WheelSpecification.objects.all()

        # Apply filters
        formNumber = request.query_params.get('formNumber')
        submittedBy = request.query_params.get('submittedBy')
        submittedDate = request.query_params.get('submittedDate')
        search = request.query_params.get('search')

        if formNumber:
            queryset = queryset.filter(formNumber=formNumber)
        if submittedBy:
            queryset = queryset.filter(submittedBy=submittedBy)
        if submittedDate:
            queryset = queryset.filter(submittedDate=submittedDate)
        if search:
            queryset = queryset.filter(formNumber__icontains=search)

        serializer = WheelSpecificationSerializer(queryset, many=True)
        return Response({
            "success": True,
            "message": f"{queryset.count()} result(s) found.",
            "data": serializer.data
        }, status=200)

# ✅ Template View: Submit wheel specification via HTML form
def submit_form(request):
    message = ''
    if request.method == 'POST':
        form = WheelSpecificationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Form submitted successfully!"
    else:
        form = WheelSpecificationForm()
    return render(request, 'api/submit.html', {'form': form, 'message': message})

# ✅ Template View: Show all saved records in table
def view_records(request):
    records = WheelSpecification.objects.all()
    return render(request, 'api/records.html', {'records': records})

# ✅ Optional: Redirect "/" to "/submit/"
def home_redirect(request):
    return redirect('submit_form')
