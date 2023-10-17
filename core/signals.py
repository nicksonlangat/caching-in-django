from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Department, Role, Employee


@receiver(post_delete, sender=Department, dispatch_uid='department_deleted')
def department_post_delete_handler(sender, **kwargs):
    cache.delete('department_objects')


@receiver(post_save, sender=Department, dispatch_uid='departments_updated')
def department_post_save_handler(sender, **kwargs):
    cache.delete('department_objects')


@receiver(post_delete, sender=Role, dispatch_uid='role_deleted')
def role_post_delete_handler(sender, **kwargs):
    cache.delete('role_objects')


@receiver(post_save, sender=Role, dispatch_uid='roles_updated')
def role_post_save_handler(sender, **kwargs):
    cache.delete('role_objects')


@receiver(post_delete, sender=Employee, dispatch_uid='employee_deleted')
def employee_post_delete_handler(sender, **kwargs):
    cache.delete('employee_objects')


@receiver(post_save, sender=Employee, dispatch_uid='employees_updated')
def employee_post_save_handler(sender, **kwargs):
    cache.delete('employee_objects')
