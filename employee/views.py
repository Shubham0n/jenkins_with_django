from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import EmployProfile
from .forms import EmployProfileForm

# List all employees
def emp_list(request):
    employees = EmployProfile.objects.all()
    return render(request, "emp_info_list.html", {"employees": employees})

# View a single employee profile
def emp_info(request, employ):
    employee = get_object_or_404(EmployProfile, slug=employ)
    return render(request, "emp_info.html", {"employee": employee})

    
# Create a new employee profile
def emp_create(request):
    if request.method == "POST":
        form = EmployProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("emp_list")
    else:
        form = EmployProfileForm()
    return render(request, "employ_profile_create.html", {"form": form})

# Update an existing employee profile
def emp_update(request, slug):
    emp = get_object_or_404(EmployProfile, slug=slug)
    if request.method == "POST":
        form = EmployProfileForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("emp_list")
    else:
        form = EmployProfileForm(instance=emp)
    return render(request, "employ_profile_update.html", {"form": form, "emp": emp})

# Delete an employee profile
def emp_delete(request, slug):
    emp = get_object_or_404(EmployProfile, slug=slug)
    if request.method == "POST":
        emp.delete()
        return redirect("emp_list")
    return render(request, "employ_profile_delete.html", {"emp": emp})
