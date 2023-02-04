from django.urls import path
from .views_API import *

urlpatterns = [
    path('api/v1/organization_list/', OrganizationAPIView.as_view())
]
