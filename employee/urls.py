from django.urls import path
from .views import home, logs, add_employee_csv, view_all_employees, get_all_employees


app_name = 'employee'

urlpatterns = [
  path('', home, name='dashboard'),
  path('employee/all', view_all_employees, name='all_employees'),
  path('employee', get_all_employees, name='get_all_employees'),
  path('add_employee', add_employee_csv, name='add_employee'),
  path('logs', logs, name='logs')
]



