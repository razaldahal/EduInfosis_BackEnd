from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'expense-category',views.ExpenseCategoryViewSet)
router.register(r'daily-expense',views.DailyExpenseViewSet)

urlpatterns = [
	path('',include(router.urls)),

	]