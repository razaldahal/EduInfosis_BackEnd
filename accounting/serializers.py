from rest_framework import serializers
from .models import *

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ('id','name','description')

class DailyExpenseSerializer(serializers.ModelSerializer):
    expense_type = serializers.IntegerField()
    class Meta:
        model = DailyExpense
        fields = ('id','expense_type','expense_detail','amount','expense_date','receipt_number')

class FeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeCategory
        fields = ('id','name','description')

class FeeAllocationSerializer(serializers.Serializer):
    fee_for = serializers.IntegerField()
    _class = serializers.IntegerField(required=False)
    fee_category = serializers.IntegerField()
    total_amount = serializers.IntegerField()
