from django.shortcuts import render,HttpResponse
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
      
      emp_form.save()
      
      context ={
        'forms': EmployeeForms(),
        'success': 'True'
      }
    else:
      
      context ={
        'forms': emp_form,
        'err': emp_form.errors.as_json(),
      }
      

  return render(request, 'employee/index.html', context)

@is_user_logged_in
def add_employee_csv(request):

  return render(request ,'employee/upload_employee.html')

@is_user_logged_in
def view_all_employees(request):
  qs = Employee.objects.all()
  context = {'data': qs}
  
  return render(request, 'employee/all_employees.html', context)
  
  
def get_all_employees(request):
  if request.method == "GET":
    emps = Employee.objects.all()
    data = serializers.serialize('json',queryset=emps, fields=('first_name', 'middle_name', 'date_of_graduation', 'date_of_employment','position', 'salary', 'supervisors', 'employee_code'))
  
    sup = serializers.serialize('json', queryset=Supervisor.objects.all())
    return JsonResponse(status=200, data={'data': data, 'supervisors': sup})
  
  
@is_user_logged_in
def logs(request):
  return render(request ,'employee/logs.html')