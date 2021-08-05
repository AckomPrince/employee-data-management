from django import forms
from .models import Employee


class EmployeeForms(forms.ModelForm):
  class Meta:
    model = Employee
    exclude = ['date_of_employment', 'employee_code']
    
    