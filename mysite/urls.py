from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments', views.DepartmentApi.as_view()),
    path('roles', views.RoleApi.as_view()),
    path('employees', views.EmployeeApi.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
]
