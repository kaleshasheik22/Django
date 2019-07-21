from django.urls import path

from .views import *

urlpatterns = [

    path('api/findByIfscCode', findByIfscCode),
    path('api/findByBankNameCity', findByBankNameCity),
 
]