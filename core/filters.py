import django_filters
from .models import *

class DepartmentEntFilter(django_filters.FilterSet):
    class Meta:
        model=dept_entre
        fields = ['department_nam_ent']
