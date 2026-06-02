from django.shortcuts import render
from complaints.models import Complaint
from leaves.models import LeaveRequest

def home(request):
    total_complaints = Complaint.objects.count()
    pending_complaints = Complaint.objects.filter(status='Pending').count()
    resolved_complaints = Complaint.objects.filter(status='Resolved').count()

    total_leaves = LeaveRequest.objects.count()
    approved_leaves = LeaveRequest.objects.filter(status='Approved').count()

    context = {
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
        'total_leaves': total_leaves,
        'approved_leaves': approved_leaves,
    }

    return render(request, 'home.html', context)