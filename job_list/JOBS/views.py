# JOBS/views.py
from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to the same view to render the updated job list
    return render(request, 'JOBS/job_list.html', {'jobs': jobs, 'form': form})
