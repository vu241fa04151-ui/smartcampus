from django.urls import path
from .views import complaint_form, view_complaints

urlpatterns = [
    path('', complaint_form, name='complaint_form'),
    path('view/', view_complaints, name='view_complaints'),
]