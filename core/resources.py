from import_export import resources
from .models import *

class ParticipantSkillResource(resources.ModelResource):
    class Meta:
        model = participant_skill
        exclude = ('id',)