from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_login = models.BooleanField(default=True)
    
    def set_password(self,raw_password):
        self.password = make_password(raw_password)
        self.save()
        
    def check_password(self, raw_password):
        return check_password(raw_password,self.password)
    
    def __str__(self):
        return self.email
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_first_name = models.CharField(max_length=255)
    customer_last_name = models.CharField(max_length=255)
    customer_designation = models.CharField(max_length=255)
    address = models.TextField()
    email_id = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=20)
    contact_type = models.CharField(max_length=100)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    msa_location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.customer_name
    
class Project(models.Model):
    master_project_id = models.AutoField(primary_key=True)
    child_project_id = models.CharField(max_length=50,unique=True)
    project_name = models.CharField(max_length=255)
    
    PROJECT_TYPE_CHOICES = [
        ('T&M','Time & Material'),
        ('Fixed Price','Fixed Price'),
    ]
    project_type = models.CharField(max_length=50,choices=PROJECT_TYPE_CHOICES)
    
    SERVICE_OFFERING_CHOICES = [
        ('Product Engineering','Product Engineering'),
        ('Staff Augmentation','Staff Augmentation'),
    ]
    
    service_offering = models.CharField(max_length=50,choices=SERVICE_OFFERING_CHOICES)
    
    PROJECT_STATUS_CHOICES = [
        ('Active','Active'),
        ('On Hold','On Hold'),
        ('Completed','Completed'),
    ]
    
    project_status = models.CharField(max_length=50,choices=PROJECT_STATUS_CHOICES)
    customer = models.ForeignKey(Customer,related_name='projects',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.project_name