from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'expense-category',views.ExpenseCategoryViewSet)
router.register(r'daily-expense',views.DailyExpenseViewSet)
router.register(r'fee-category',views.FeeCategoryViewSet)
router.register(r'fee-allocation',views.FeeAllocationViewSet)

urlpatterns = [
	path('',include(router.urls)),

	]