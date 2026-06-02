from django.urls import path
from .views import leave_form, view_leaves

urlpatterns = [
    path('', leave_form, name='leave_form'),
    path('view/', view_leaves, name='view_leaves'),
]