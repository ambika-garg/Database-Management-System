from django.contrib import admin
from .models import category
from .models import dept_entre, dept_aware, dept_capac
from .models import dept_skill
from .models import program_entre, program_capac, program_aware
from .models import program_skill
from .models import participant_entre, participant_aware, participant_capac
from .models import participant_skill
from .models import placement_skill
from import_export.admin import ImportExportModelAdmin

@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_entre)
class DepartmentEntAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_aware)
class DepartmentawareAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_capac)
class DepartmentcapacAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_skill)
class DepartmentSkillAdmin(ImportExportModelAdmin):
    pass

@admin.register(program_aware)
class ProgramawareAdmin(ImportExportModelAdmin):
    pass

@admin.register(program_capac)
class ProgramCapacAdmin(ImportExportModelAdmin):
    pass

@admin.register(program_entre)
class ProgramEntAdmin(ImportExportModelAdmin):
    pass

@admin.register(program_skill)
class ProgramSkillAdmin(ImportExportModelAdmin):
    pass

@admin.register(participant_entre)
class ParticipantEntAdmin(ImportExportModelAdmin):
    pass

@admin.register(participant_skill)
class ParticipantSkillAdmin(ImportExportModelAdmin):
    pass

@admin.register(participant_aware)
class ParticipantAwareAdmin(ImportExportModelAdmin):
    pass

@admin.register(participant_capac)
class ParticipantCapacAdmin(ImportExportModelAdmin):
    pass

@admin.register(placement_skill)
class PlacementSkillAdmin(ImportExportModelAdmin):
    pass