from django.urls import path
from .views import (
    WheelSpecificationCreateView,
    WheelSpecificationListView,
    submit_form,
    view_records,
    home_redirect,  # include this
)

urlpatterns = [
    path('', home_redirect),  # root path → redirects to /submit/
    path('wheel-specifications/', WheelSpecificationCreateView.as_view(), name='create_wheel'),
    path('wheel-specifications', WheelSpecificationListView.as_view(), name='get_wheel'),
    path('submit/', submit_form, name='submit_form'),
    path('records/', view_records, name='view_records'),
]
