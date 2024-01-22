from django.shortcuts import render, redirect
from .models import Job
from .models import Company
from .forms import adminform

def Home(request):
    data = Job.objects.all()
    form = adminform()
    
    if request.method == 'POST':
        form = adminform(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the view displaying the table after successful form submission
            return redirect('view')
    
    return render(request, 'index.html', {'stu': data, 'form': form})

def Edit(request, pk):
    site = Job.objects.get(id=pk)
    data = Job.objects.all()
    form = adminform(instance=site)
    
    if request.method == 'POST':
        form = adminform(request.POST, instance=site)
        if form.is_valid():
            form.save()
            # Redirect to the view displaying the table after successful form submission
            return redirect('view')

    return render(request, 'index.html', {'stu': data, 'form': form})

def Delete(request, pk):
    site = Job.objects.get(id=pk)
    site.delete()
    return redirect('view')
