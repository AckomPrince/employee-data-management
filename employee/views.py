import secrets
import string

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import EmployeeForms
from .decorators import is_user_logged_in
from django.core import serializers
from .models import Employee, Supervisor


# Create your views here.


@is_user_logged_in
def home(request):
    forms = EmployeeForms()
    context = {
        'forms': forms,
    }

    if request.method == 'POST':
        request_data = request.POST

        emp_form = EmployeeForms(request_data)

        if emp_form.is_valid():
            clean_data = emp_form.cleaned_data

            first_name = clean_data['first_name']
            last_name = clean_data['last_name']
            emp_form.save()

            base_username = f"{first_name.lower()}.{last_name.lower()}"
            password = generate_random_password()
            user = User.objects.create_user( password=password, username=base_username)
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 message=f"New Employee Added Successfully. Username : {base_username} -And- "
                                         f"Password : {password}")
            return view_all_employees(request)

        context = {
            'forms': emp_form,
            'err': emp_form.errors.as_json(),
        }

    return render(request, 'employee/index.html', context)


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@is_user_logged_in
def add_employee_csv(request):
    return render(request, 'employee/upload_employee.html')


@is_user_logged_in
def view_all_employees(request):
    qs = Employee.objects.all()
    return render(request, 'employee/list_employees.html',
                  {'data': qs})


@is_user_logged_in
def delete_employment(request, employee_id):
    employee = Employee.objects.filter(id=employee_id).delete()
    messages.add_message(request, messages.SUCCESS,
                         message="Employee Deleted Successfully.")
    return view_all_employees(request)


@is_user_logged_in
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 message="Employee Updated Successfully.")
            return redirect('employee:all_employees')

    form = EmployeeForms(instance=employee)

    return render(request, 'employee/index.html', {'forms': form, 'employee': employee})


def get_all_employees(request):
    if request.method == "GET":
        emps = Employee.objects.all()
        data = serializers.serialize('json', queryset=emps, fields=(
            'first_name', 'middle_name', 'date_of_graduation', 'date_of_employment', 'position', 'salary',
            'supervisors',
            'employee_code'))

        sup = serializers.serialize('json', queryset=Supervisor.objects.all())
        return JsonResponse(status=200, data={'data': data, 'supervisors': sup})


@is_user_logged_in
def logs(request):
    return render(request, 'employee/logs.html')
