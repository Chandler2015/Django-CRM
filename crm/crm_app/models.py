from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime,timezone
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User

class Customer(User):
    INDUSTRY_CHOICES = [
        ('OIL/GAS','oil/gas'),
        ('FARMING','farming'),
        ('CONSTRUCTION','construction'),
    ]

    WHERE_TO_HEAR_CHOICES = [
        ('SOCIAL','social media'),
        ('NEWS','newspaper'),
        ('GOOGLE','google'),
        ('FRIENDS','friends'),
    ]
   
    phone_number = PhoneNumberField(blank = True)
    address = models.CharField(max_length= 200,blank=True)
    industry = models.CharField(
        max_length= 20,
        choices = INDUSTRY_CHOICES,
        default = 'OIL/GAS',
    )
    where_to_hear = models.CharField(
        max_length= 20,
        choices = WHERE_TO_HEAR_CHOICES,
        default = 'SOCIAL',
    ) 

    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.username

class Task(models.Model):
    TASK_TYPE_CHOICES = [
        ('CALL','call'),
        ('EMAIL','email'),
        ('TEXT','text'),
    ]

    sales_rep = models.ForeignKey(User, on_delete=models.CASCADE,blank = True,null= True,related_name = 'User',default= 1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank = True,null= True,related_name = 'customer' )
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(
        max_length= 50,
        choices = TASK_TYPE_CHOICES,
        default = 'CALL',
    )
    follow_up_date = models.DateField(blank = True,null = True) 
    notes = models.TextField(blank = True)
    is_finished = models.BooleanField(default = False)


    @property
    def short_notes(self):
        return truncatechars(self.notes, 50)





