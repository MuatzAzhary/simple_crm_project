from django.db import models
from django.utils import timezone


# Activity Types
class Activity_type(models.Model):
    type_name = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.type_name

# Employees
class Employee(models.Model):
    full_name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

# Customers 
class Customer(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'A','Active'
        UNACTIVE = 'UA','Un Active'

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    company = models.CharField(max_length=300)
    status = models.CharField(max_length=2,choices=Status.choices , default=Status.ACTIVE)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Activities
class Activity(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    activity_type = models.ForeignKey(Activity_type,on_delete=models.CASCADE)
    note = models.TextField(default="")
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Activity {self.id}'


