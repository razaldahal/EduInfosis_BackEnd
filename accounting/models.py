from django.db import models
from main.models import BaseModel
from academics.models import Class

class ExpenseCategory(BaseModel):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

class DailyExpense(BaseModel):
    expense_type = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)
    expense_detail = models.CharField(max_length=120)
    amount = models.IntegerField()
    expense_date = models.DateField()
    receipt_number = models.IntegerField(null=True,blank=True)

class FeeCategory(BaseModel):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)

class FeeAllocation(BaseModel):
    fee_category = models.ForeignKey(FeeCategory,on_delete=models.CASCADE)
    _class = models.ForeignKey(Class,on_delete=models.CASCADE)
    total_amount = models.IntegerField()