# from django.contrib import admin
# from .models import category
# from .models import dept_entre
# from .models import dept_skill
# from .models import program_entre
# from .models import program_skill
# from .models import participant_entre
# from .models import participant_skill
# from .models import placement_skill
#
# @admin.register(category)
# class Category(category):
#     list_display = [field.name for field in category.meta.get_fields()]
#
# @admin.register(dept_entre)
# class DepartmentEnt(dept_entre):
#     list_display = [field.name for field in dept_entre.meta.get_fields()]
#
# @admin.register(dept_skill)
# class DepartmentSkill(dept_skill):
#     list_display = [field.name for field in dept_skill.meta.get_fields()]
#
# @admin.register(program_entre)
# class ProgramEnt(program_entre):
#     list_display = [field.name for field in program_entre.meta.get_fields()]
#
# @admin.register(program_skill)
# class ProgramSkill(program_skill):
#     list_display = [field.name for field in program_skill.meta.get_fields()]
#
# @admin.register(participant_entre)
# class ParticipantEnt(participant_entre):
#     list_display = [field.name for field in participant_entre.meta.get_fields()]
#
# @admin.register(participant_skill)
# class ParticipantSkill(participant_skill):
#     list_display = [field.name for field in participant_skill.meta.get_fields()]
#
# @admin.register(placement_skill)
# class PlacementSkill(placement_skill):
#     list_display = [field.name for field in placement_skill.meta.get_fields()]