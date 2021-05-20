import django_filters
from .models import *

class program_skillFilter(django_filters.FilterSet):
    program_name_skill = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = program_skill
        fields = ['state','financial_Year_skill']