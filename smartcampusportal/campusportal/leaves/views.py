from django.shortcuts import render, redirect
from .models import LeaveRequest

def leave_form(request):

    if request.method == 'POST':
        reason = request.POST['reason']
        from_date = request.POST['from_date']
        to_date = request.POST['to_date']

        LeaveRequest.objects.create(
            reason=reason,
            from_date=from_date,
            to_date=to_date
        )

        return redirect('/leave/')

    return render(request, 'leave_form.html')
def view_leaves(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'view_leaves.html', {'leaves': leaves})