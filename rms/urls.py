from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bldc/', views.bldc, name='bldc_projects'),
    path('search/', views.search, name='searchid'),
    path('dayReport/', views.dayR, name='dayRep'),
    path('monthReport/', views.monthR, name='monthRep'),
    path('openId/<System_RID_No>/', views.openId, name='IdDtls'),
    path('GetInvDaysData/', views.GetInvDaysData, name='apiDayData'),
    path('GetInvMonthData/', views.GetInvMonthData, name='apiMonthData'),
]