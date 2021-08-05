from django.db import models
import secrets
# Create your models here.



class Supervisor(models.Model):
  employee_id = models.CharField(max_length=20)
  first_name = models.CharField(max_length=150)
  middle_name = models.CharField(max_length=150)
  
  def __str__(self):
    return self.first_name
  
  
    
class Employee(models.Model):
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  date_of_graduation = models.DateField()
  date_of_employment = models.DateField(auto_now=True)
  position = models.CharField(max_length=100)
  salary = models.DecimalField(decimal_places=3, max_digits=8)
  supervisors = models.ManyToManyField(Supervisor, blank=True)
  employee_code =  models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return str(self.employee_initials)
  
  
  @property
  def employee_initials(self):
    return self.create_employee_code
  
  @property
  def create_employee_code(self):
    code = '{}{}-{}'.format(self.first_name[0].upper(), self.middle_name[0].upper(), str(secrets.randbits(20))[:3])
    return code
  
  @property
  def employee_supervisors_all(self):
    sup = self.supervisors.all()
    all_sup = []
    
    for s in sup:
      all_sup.append(s.first_name)
    # print(all_sup)
    return all_sup
  
  
  

  
  
  
  
class Log(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True)
  no_employee_records = models.IntegerField()
  status = models.BooleanField(default=False)
  errors = models.TextField()
  
  def __str__(self):
    return str(self.pk)
  
