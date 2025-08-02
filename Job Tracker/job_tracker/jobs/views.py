from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)
    return render(request,'jobs/job_list.html',{'jobs':jobs})

@login_required
def job_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render (request, 'jobs/job_form.html', {'form':form})

@login_required
def job_edit(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user = request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form':form})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request,'jobs/job_confirm_delete.html',{'job':job})