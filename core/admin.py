from django.contrib import admin
from .models import category
from .models import dept_entre
from .models import dept_skill
from .models import program_entre
from .models import program_skill
from .models import participant_entre
from .models import participant_skill
from .models import placement_skill
from import_export.admin import ImportExportModelAdmin

@admin.register(category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_entre)
class DepartmentEntAdmin(ImportExportModelAdmin):
    pass

@admin.register(dept_skill)
class DepartmentSkillAdmin(ImportExportModelAdmin):
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

@admin.register(placement_skill)
class PlacementSkillAdmin(ImportExportModelAdmin):
    pass