from django.db.models.signals import post_save
from django.dispatch import receiver
import secrets

from .models import Supervisor, Employee, Log

def create_employee_code(first_name, middle_name):
  code = '{}{}-{}'.format(first_name[0].upper(), middle_name[0].upper(), str(secrets.randbits(20))[:3])
  return code

@receiver(sender=Employee, signal=post_save)
def create_supervisor_signal(sender,instance, created, **kwargs):
  if created:
    emp = Employee.objects.get(pk=instance.pk)
    emp.employee_code= instance.create_employee_code
    emp.save()
    
    print('Created Employee', instance)
    supervisor = Supervisor.objects.create(employee_id = instance.id, first_name=instance.first_name, middle_name=instance.middle_name)
    supervisor.save()
    
    # Log.objects.create()