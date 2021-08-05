from django.test import TestCase

# Create your tests here.
from .models import Supervisor, Employee, Log
import datetime


class TestEmployeeModel (TestCase):
  
  @classmethod
  def setUp(cls):
    employee = Employee.objects.create(first_name='John', middle_name='Doe', date_of_graduation=datetime, position='Developer')
    
    employee.save()
    
    
  def test_employee(self):
    employee = Employee.objects.get(id=1)
    self.assertEqual('John', employee.first_name)