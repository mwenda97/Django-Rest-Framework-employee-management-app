from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'Deps',DepartmentView,'Dep')
router.register(r'Emps',EmployeeView,'Emp')

urlpatterns = [
    path('',include(router.urls))
]
