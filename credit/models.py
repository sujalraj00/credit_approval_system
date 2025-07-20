from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    monthly_salary= models.FloatField()
    approved_limit= models.FloatField()
    phone_number=models.BigIntegerField(unique=True)


class Loan(models.Model): 
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount= models.FloatField()
    tenure= models.IntegerField()
    interest_rate= models.FloatField()
    monthly_repayment= models.FloatField()
    start_date= models.DateField(auto_now_add=True)
    end_date= models.DateField()
    emis_paid_on_time= models.IntegerField()

