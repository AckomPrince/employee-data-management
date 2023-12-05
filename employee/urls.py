from django.urls import path
from .views import home, logs, add_employee_csv, view_all_employees, get_all_employees, delete_employment, update_employee


app_name = 'employee'

urlpatterns = [
  path('', home, name='dashboard'),
  path('employee/all', view_all_employees, name='all_employees'),
  path('employee/<employee_id>/delete', delete_employment, name = "delete_employee"),
  path('update/<employee_id>/employee', update_employee, name = "update_employee"),
  path('employee', get_all_employees, name='get_all_employees'),
  path('add_employee', add_employee_csv, name='add_employee'),
  path('logs', logs, name='logs')
]



