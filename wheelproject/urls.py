from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                  # Django admin
    path('api/forms/', include('api.urls')),          # Backend API endpoints
    path('', include('api.urls')),                    # Frontend views (submit/ and records/)
]
