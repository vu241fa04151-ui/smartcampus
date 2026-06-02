from django.shortcuts import render, redirect
from .models import Complaint

def complaint_form(request):

    if request.method == 'POST':
        student_name = request.POST['student_name']
        room_number = request.POST['room_number']
        title = request.POST['title']
        category = request.POST['category']
        description = request.POST['description']
        priority = request.POST['priority']

        Complaint.objects.create(
            student_name=student_name,
            room_number=room_number,
            title=title,
            category=category,
            description=description,
            priority=priority
)

        return redirect('/complaint/')

    return render(request, 'complaint_form.html')
def view_complaints(request):
    complaints = Complaint.objects.all()
    return render(
        request,
        'view_complaints.html',
        {'complaints': complaints}
    )

def view_complaints(request):

    search = request.GET.get('search')

    if search:
        complaints = Complaint.objects.filter(title__icontains=search)
    else:
        complaints = Complaint.objects.all()

    return render(
        request,
        'view_complaints.html',
        {'complaints': complaints}
    )