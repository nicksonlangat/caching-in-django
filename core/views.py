from rest_framework.views import APIView

from .pagination import (
    PageNumberPagination, get_paginated_response
)


from .selectors import (
    department_list,
    employee_list,
    role_list
)
from .serializers import (
    DepartmentSerializer,
    RoleSerializer,
    EmployeeSerializer
)


class DepartmentApi(APIView):
    """
    API endpoint to:

    1. List all departments in the database

    Requires:
    No Authentication
    """

    class Pagination(PageNumberPagination):
        default_limit = 25

    permission_classes = []

    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        qs = department_list()

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )


class RoleApi(APIView):
    """
    API endpoint to:

    1. List all roles in the database

    Requires:
    No Authentication
    """

    class Pagination(PageNumberPagination):
        default_limit = 25

    permission_classes = []

    serializer_class = RoleSerializer

    def get(self, request, *args, **kwargs):
        qs = role_list()

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )


class EmployeeApi(APIView):
    """
    API endpoint to:

    1. List all employees in the database

    Requires:
    No Authentication
    """

    class Pagination(PageNumberPagination):
        page_size = 50

    permission_classes = []

    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        qs = employee_list()

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.serializer_class,
            queryset=qs,
            request=request,
            view=self,
        )
