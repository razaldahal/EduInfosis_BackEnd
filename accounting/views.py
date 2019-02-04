from rest_framework import viewsets,serializers,status
from rest_framework.response import Response


from .serializers import *
from .models import *

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class DailyExpenseViewSet(viewsets.ViewSet):
    queryset = DailyExpense.objects.all()

    def create(self,request):
        serializer = DailyExpenseSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            print(data)
            obj  = DailyExpense.objects.create(expense_type_id = data['expense_type'],
                    expense_detail = data['expense_detail'],
                    amount = data['amount'],
                    expense_date = data['expense_date'],
                    receipt_number = data['receipt_number']
            )
           
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            raise serializers.ValidationError(
                {'Detail':[serializer.errors]}
            )

    def list(self,request):
        objects = self.queryset
        output = []
        for obj in objects:
            temp ={
                'id':obj.id,
                'expense_type':obj.expense_type.name,
                'amount':obj.amount,
                'expense_date':obj.expense_date,
                
            }
            output.append(temp)
        return Response(output,status=status.HTTP_200_OK)

    def get_object(self,pk):
        return DailyExpense.objects.get(id = pk)

    def retrieve(self,request,pk):
        obj = self.get_object(pk)
        temp ={
            'id':obj.id,
            'expense_type':obj.expense_type.id,
            'amount':obj.amount,
            'expense_date':obj.expense_date,
            'expense_detail':obj.expense_detail,
            'receipt_number':obj.receipt_number,
            
        }
        return Response(temp,status=status.HTTP_200_OK)

    def update(self,request,pk):
        obj = self.get_object(pk)
        serializer = DailyExpenseSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            print(data)
            obj.expense_type_id = data.get('expense_type',obj.expense_type)
            obj.expense_detail = data.get('expense_detail',obj.expense_detail)
            obj.amount = data.get('amount',obj.amount)
            obj.expense_date = data.get('expense_date',obj.expense_date)
            obj.receipt_number = data.get('receipt_number',obj.receipt_number)
            obj.save()

            return Response(data,status=status.HTTP_201_CREATED)
        raise serializers.ValidationError({
            "detail":[serializer.errors]
        })

    
class FeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = FeeCategory.objects.all()
    serializer_class = FeeCategorySerializer

class FeeAllocationViewSet(viewsets.ViewSet):
    queryset = FeeAllocation.objects.all()

    def create(self,request):
        serializer = FeeAllocationSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            fee_for = data['fee_for']

            if fee_for==2:
                obj.c = FeeAllocation.objects.get_or_create(fee_category=data['fee_category'],
                                                            _class_id = data['_class'],
                                                            defaults = {
                                                                'total_amount':data['total_amount']
                                                            })
            return Response("kdshdj")
        else:
            raise serializers.ValidationError({
                'Detail':[serializer.errors]
            })




			
