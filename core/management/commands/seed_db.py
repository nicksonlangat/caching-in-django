import json
from pathlib import Path
import random

from django.core.management.base import BaseCommand

from ...models import Department, Role, Employee


class Command(BaseCommand):
    help = 'Adds initial data to the database'

    def handle(self, *args, **options):
        departments_filepath = (Path(__file__).parent).joinpath('departments.json')
        roles_filepath = (Path(__file__).parent).joinpath('roles.json')
        employees_filepath = (Path(__file__).parent).joinpath('employees.json')

        with open(departments_filepath) as f:
            data = json.load(f)
            for department in data:
                Department.objects.create(name=department['name'])

        with open(roles_filepath) as f:
            data = json.load(f)
            for role in data:
                Role.objects.create(name=role['name'])

        departments = [department for department in Department.objects.all()]
        roles = [role.id for role in Role.objects.all()]

        with open(employees_filepath) as f:
            data = json.load(f)
            for employee in data:
                employee = Employee.objects.create(
                    first_name=employee['first_name'],
                    last_name=employee['last_name'],
                    department=random.choice(departments),
                )
                employee.roles.set([random.choice(roles) for i in range(10)])
                employee.save()

        self.stdout.write('Seed data added to the db successfully.')
