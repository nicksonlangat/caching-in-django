from django.db.models.query import QuerySet
from django.core.cache import cache
from .models import Department, Role, Employee


def department_list() -> QuerySet[Department]:

    department_objects = cache.get('department_objects')

    if department_objects is None:
        department_objects = Department.objects.all()
        cache.set('department_objects', department_objects)

    return department_objects


def role_list() -> QuerySet[Role]:
    role_objects = cache.get('role_objects')

    if role_objects is None:
        role_objects = Role.objects.all()
        cache.set('role_objects', role_objects)

    return role_objects


def employee_list() -> QuerySet[Employee]:

    employee_objects = cache.get('employee_objects')

    if employee_objects is None:
        employee_objects = Employee.objects.select_related('department').prefetch_related('roles')
        cache.set('employee_objects', employee_objects)

    return employee_objects
