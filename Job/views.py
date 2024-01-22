from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .forms import JobApplicationForm
from Admin.models import Job
from Admin.models import Company
from .models import AppliedJob
from .forms import SearchForm

def Index(request):      
    return render(request, 'home.html')
    

def Home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('view')  # Redirect to 'view' URL
        else:
            # Handle incorrect credentials here
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def View(request):
    data=Job.objects.all()
    company=request.GET.get("company")
    if company!="" and company is not None:
        data=Job.objects.filter(company__company_name__icontains=company)
       
    return render(request,'view.html',{'adi':data})
    # return render(request,'view.html')

def Register(request):
    form = LoginForm()
    context = {'form': form}

    if request.method == "POST":
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')  # Redirect to 'login' URL after successful registration

    return render(request, 'register.html', context)

def Job_Position(request,pk):
    data=Job.objects.get(id=pk)
    return render(request,'jobdetails.html',{'adi':data})
def Company_details(request,pk):
    data=Company.objects.get(id=pk)
    return render(request,'company.html',{'com':data})

def Logout(request):
    logout(request)
    return redirect('home')
def Companylist(request):
    data=Company.objects.all()
    return render(request,'list.html',{'list':data})
def Joblist(request):
    data=Job.objects.all()
    return render(request,'job_list.html',{'joblist':data})

def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            cover_letter = form.cleaned_data['cover_letter']
            resume = form.cleaned_data['resume']
            applied_job=AppliedJob.objects.create(user=user, job=job, cover_letter=cover_letter, resume=resume)
            return redirect('success_page', applied_job_id=applied_job.id) 
    else:
        form = JobApplicationForm()

    return render(request, 'apply_job.html', {'form': form, 'job': job})

def success_page(request,applied_job_id):
     applied_job = AppliedJob.objects.get(id=applied_job_id)
     return render(request, 'success_page.html', {'applied_job': applied_job})

# def Jobcategory():
#     data=Job.objects.get.all()
#     jobcategory = request.GET.get("jobcategory")
#     if jobcategory!="" and jobcategory is not None:
#         data =Job.objects.filter(jobcategory_job_position_icontains=jobcategory)
       
#     return render(request,'profile.html',{'std':data})
# def search_results(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             search_query = form.cleaned_data['search_query']
#             # Perform your search logic here using the search_query
#             # For example, if you have a 'YourModel' you want to search in:
#             results = Job.objects.filter(job_position__icontains=search_query)
#             return render(request, 'search_results.html', {'results': results, 'query': search_query})
#     else:
#         form = SearchForm()
#     return render(request, 'view.html', {'form': form})

def Jobcategory(request):
    data=Job.objects.all()
    jobcategory = request.GET.get("jobcategory")
    if jobcategory!="" and jobcategory is not None:
        data =Job.objects.filter(job_position__icontains=jobcategory)
       
    return render(request,'view.html',{'form':data})

    
