import django_filters

from django.forms.widgets import TextInput
from .models import *

#------------------------------------------------------------SKILL FILTERS------------------------------------------------------
class program_skillFilter(django_filters.FilterSet):
    program_name_skill = django_filters.ModelChoiceFilter(queryset=program_skill.objects.all() , empty_label = "Select Program Name")
    depart_name_skill = django_filters.ModelChoiceFilter(queryset = dept_skill.objects.all(),  empty_label = 'Department Name')
    state = django_filters.CharFilter(field_name="state",
                                                      widget=TextInput(attrs={'placeholder': 'State'}),
                                                      lookup_expr='icontains')
    financial_Year_skill = django_filters.CharFilter(field_name="financial_Year_skill",
                                                      widget=TextInput(attrs={'placeholder': 'Financial Year (YY-YY)'}),
                                                      lookup_expr='icontains')

    class Meta:
        model = program_skill
        fields = ['state','financial_Year_skill']


class department_skillFilter(django_filters.FilterSet):
    department_name_skill = django_filters.CharFilter(field_name="department_name_skill", widget=TextInput(attrs={'placeholder': 'Department Name'}), lookup_expr='icontains')
    class Meta:
        model = dept_skill
        fields = ['department_name_skill' ]

class participant_skillFilter(django_filters.FilterSet):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))

    name_skill = django_filters.CharFilter(field_name="name_skill_FirstName",
                                                      widget=TextInput(attrs={'placeholder': 'First Name'}),
                                                      lookup_expr='icontains')

    program_id_skill = django_filters.ModelChoiceFilter(queryset=program_skill.objects.all(),empty_label = 'Program Name')
    gender = django_filters.ChoiceFilter(choices = GENDER_CHOICES, empty_label ='Gender')
    category = django_filters.ChoiceFilter(choices = CATEGORY_CHOICES, empty_label = 'Category')

    class Meta:
        model = participant_skill
        fields = ['name_skill', 'program_id_skill', 'gender', 'category']

class placement_skillFilter(django_filters.FilterSet):
    CHOICE = (('Yes', 'Yes'), ('No', 'No'))
    placement_status = django_filters.ChoiceFilter(choices = CHOICE, empty_label ='Placement Status')
    participant_id_skill = django_filters.ModelChoiceFilter(queryset=participant_skill.objects.all(), empty_label = "Participant ID")
    placement_id_rced_batch_id = django_filters.NumberFilter(field_name="placement_id_rced_batch_id",widget=TextInput(attrs={'placeholder': 'RCED BATCH ID'}),
                                                      lookup_expr='iexact')
    class Meta:
        model = placement_skill
        fields = ['participant_id_skill', 'placement_id_rced_batch_id', 'placement_status']



#-----------------------------------------------------ENTERPENEURSHIP FILTERS---------------------------------------------------
class department_ENTFilter(django_filters.FilterSet):
    department_nam_ent = django_filters.CharFilter(field_name="department_nam_ent", widget=TextInput(attrs={'placeholder': 'Department Name'}), lookup_expr='icontains')
    class Meta:
        model = dept_entre
        fields = ['department_nam_ent']

class program_ENTFilter(django_filters.FilterSet):
    program_name_ent = django_filters.ModelChoiceFilter(queryset=program_entre.objects.all() , empty_label = "Select Program Name")
    depart_name_ent = django_filters.ModelChoiceFilter(queryset = dept_entre.objects.all(),  empty_label = 'Department Name')
    state_ent = django_filters.CharFilter(field_name="state_ent",
                                                      widget=TextInput(attrs={'placeholder': 'State'}),
                                                      lookup_expr='icontains')
    financial_year_ent = django_filters.CharFilter(field_name="financial_year_ent",
                                                      widget=TextInput(attrs={'placeholder': 'Financial Year (YY-YY)'}),
                                                      lookup_expr='icontains')

    class Meta:
        model = program_entre
        fields = ['state_ent','financial_year_ent']


class participant_ENTFilter(django_filters.FilterSet):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))

    name_of_trainee =  django_filters.CharFilter(field_name="name_of_trainee",
                                                      widget=TextInput(attrs={'placeholder': 'Name of Trainee'}),
                                                      lookup_expr='icontains')

    program_id_ent = django_filters.ModelChoiceFilter(queryset=program_entre.objects.all(),empty_label = 'Program Name')
    gender = django_filters.ChoiceFilter(choices = GENDER_CHOICES, empty_label ='Gender')
    category_entre = django_filters.ChoiceFilter(choices = CATEGORY_CHOICES, empty_label = 'Category')

    class Meta:
        model = participant_entre
        fields = ['name_of_trainee', 'program_id_ent', 'gender', 'category_entre']

#-----------------------------------------------------AWARENESS FILTERS---------------------------------------------------
class program_awareFilter(django_filters.FilterSet):
    program_name_aware = django_filters.ModelChoiceFilter(queryset=program_aware.objects.all() , empty_label = "Select Program Name")
    depart_name_aware = django_filters.ModelChoiceFilter(queryset = dept_aware.objects.all(),  empty_label = 'Department Name')
    state = django_filters.CharFilter(field_name="state",
                                                      widget=TextInput(attrs={'placeholder': 'State'}),
                                                      lookup_expr='icontains')
    financial_year_aware = django_filters.CharFilter(field_name="financial_year_aware",
                                                      widget=TextInput(attrs={'placeholder': 'Financial Year (YY-YY)'}),
                                                      lookup_expr='icontains')

    class Meta:
        model = program_aware
        fields = ['state','financial_year_aware']


class department_awareFilter(django_filters.FilterSet):
    department_name_aware = django_filters.CharFilter(field_name="department_name_aware", widget=TextInput(attrs={'placeholder': 'Department Name'}), lookup_expr='icontains')
    class Meta:
        model = dept_aware
        fields = ['department_name_aware' ]

class participant_awareFilter(django_filters.FilterSet):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))

    name_of_trainee = django_filters.CharFilter(field_name="name_of_trainee",
                                                      widget=TextInput(attrs={'placeholder': 'Name of Trainee'}),
                                                      lookup_expr='icontains')

    program_id_aware = django_filters.ModelChoiceFilter(queryset=program_aware.objects.all(),empty_label = 'Program Name')
    gender = django_filters.ChoiceFilter(choices = GENDER_CHOICES, empty_label ='Gender')
    category_aware = django_filters.ChoiceFilter(choices = CATEGORY_CHOICES, empty_label = 'Category')

    class Meta:
        model = participant_aware
        fields = ['name_of_trainee', 'program_id_aware', 'gender', 'category_aware']

#-----------------------------------------------------CAPACITY FILTERS---------------------------------------------------
class department_capacFilter(django_filters.FilterSet):
    department_name_capac = django_filters.CharFilter(field_name="department_name_capac", widget=TextInput(attrs={'placeholder': 'Department Name'}), lookup_expr='icontains')
    class Meta:
        model = dept_capac
        fields = ['department_name_capac']

class program_capacFilter(django_filters.FilterSet):
    program_name_capac = django_filters.ModelChoiceFilter(queryset=program_capac.objects.all() , empty_label = "Select Program Name")
    depart_name_capac = django_filters.ModelChoiceFilter(queryset = dept_capac.objects.all(),  empty_label = 'Department Name')
    state_capac = django_filters.CharFilter(field_name="state_capac",
                                                      widget=TextInput(attrs={'placeholder': 'State'}),
                                                      lookup_expr='icontains')
    financial_year_capac = django_filters.CharFilter(field_name="financial_year_capac",
                                                      widget=TextInput(attrs={'placeholder': 'Financial Year (YY-YY)'}),
                                                      lookup_expr='icontains')

    class Meta:
        model = program_capac
        fields = ['state_capac','financial_year_capac']


class participant_capacFilter(django_filters.FilterSet):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
    CATEGORY_CHOICES = (('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'))

    name_of_trainee =  django_filters.CharFilter(field_name="name_of_trainee",
                                                      widget=TextInput(attrs={'placeholder': 'Name of Trainee'}),
                                                      lookup_expr='icontains')

    program_id_capac = django_filters.ModelChoiceFilter(queryset=program_capac.objects.all(),empty_label = 'Program Name')
    gender = django_filters.ChoiceFilter(choices = GENDER_CHOICES, empty_label ='Gender')
    category_capac = django_filters.ChoiceFilter(choices = CATEGORY_CHOICES, empty_label = 'Category')

    class Meta:
        model = participant_capac
        fields = ['name_of_trainee', 'program_id_capac', 'gender', 'category_capac']

