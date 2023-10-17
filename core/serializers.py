from rest_framework import serializers

from .models import Department, Employee, Role


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id", "name",
            "created", "updated"
        ]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "id", "name",
            "created", "updated"
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id", "first_name", "last_name",
            "department", "roles", "created",
            "updated"
        ]

    def to_representation(self, instance):
        data = super(EmployeeSerializer, self).to_representation(instance)
        data["department"] = DepartmentSerializer(instance.department).data
        data["roles"] = RoleSerializer(instance.roles.all(), many=True).data
        return data
