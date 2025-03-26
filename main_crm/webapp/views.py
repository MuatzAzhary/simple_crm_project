from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseNotFound

# Create your views here.
# get summary in the dashboard

def index(request):
    return render(request,'webapp/index.html')

@login_required(login_url='login')
def dashboard(request):
    activities = Activity.objects.all().count
    employees = Employee.objects.all().count
    customers = Customer.objects.all().count

    summary_totals = {
        'Actitvitis' : activities,
        'Employees' : employees,
        'Customers' : customers
    }

    return render(request,'webapp/dashboard.html',{'summary':summary_totals})


# Get Activities in table
@login_required(login_url='login')
def get_activities(request):
    activities = Activity.objects.all()

    return render(request,'webapp/activities.html',{'activities':activities})

# get one activity detail
@login_required(login_url='login')
def get_activity(request, activity_id):
    try :
        activity = Activity.objects.get(id=activity_id)
        return render(request,'webapp/activity.html',{'activity':activity})
    except :
        raise(HttpResponseNotFound())


# Get Customers in table
@login_required(login_url='login')
def get_customers(request):
    customers = Customer.objects.all()

    return render(request,'webapp/customers.html',{'customers':customers})

# Get Employees in table
@login_required(login_url='login')
def get_employees(request):
    employees = Employee.objects.all()

    return render(request,'webapp/employees.html',{'employees':employees})


# Register new user 
def register(request):
    form = createuserform
    if request.method == 'POST' :
        form = createuserform(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('login')
    else :
        form = createuserform()

    return render(request,'webapp/register.html',{'form':form})


# login 
def Login(request):
    form = loginform()

    if request.method == 'POST' :
        form = loginform(request,data=request.POST)
        if form.is_valid() :
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None :
                login(request,user)
                return redirect('dashboard')
    else :
        form = loginform()
    
    return render(request,'webapp/login.html',{'form':form})


# logout
def log_out(request):
    logout(request)
    return redirect('home')

# create employee
@login_required(login_url='login')
def createnew_employee(request):
    form = create_employee()
    if request.method == 'POST':
        form = create_employee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = create_employee()
    
    return render(request,'webapp/create_employee.html',{'form':form})

# create customer
@login_required(login_url='login')
def createnew_customer(request):
    form = create_customer()
    if request.method == "POST" :
        form = create_customer(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('customers')
    else :
        form = create_customer()

    return render(request,'webapp/create_customer.html',{'form':form})

# create activity
@login_required(login_url='login')
def createnew_activity(request):
    form = create_activity()
    if request.method == 'POST' :
        form = create_activity(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('activities')
    else :
        form = create_activity()

    return render(request,'webapp/create_activity.html',{'form':form})

# create activity-type
@login_required(login_url='login')
def createnew_activitytype(request):
    form = create_activitytype()
    if request.method == 'POST' :
        form = create_activitytype(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else :
        form = create_activitytype()
    
    return render(request,'webapp/create_activitytype.html',{'form':form})


# update activity 
@login_required(login_url='login')
def updatethe_activity(request, activity_id):
    activity = get_object_or_404(Activity,id=activity_id)
    form = update_activity(instance=activity)
    if request.method == 'POST' :
        form = update_activity(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activities')
        
    return render(request,'webapp/update_activity.html',{'form':form})

# delete activity 
@login_required(login_url='login')
def delete_activity(request,activity_id):
    activity = get_object_or_404(Activity,id=activity_id)
    activity.delete()
    return redirect('activities')


def not_found_page(request,exception):
    return render(request,'webapp/404.html',status=404)