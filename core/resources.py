from import_export import resources
from .models import *

class ParticipantEntAdminResource(resources.ModelResource):
    class Meta:
        model = participant_entre
        exclude = ('id',)

class ParticipantSkillAdminResource(resources.ModelResource):
    class Meta:
        model = participant_skill
        exclude = ('id',)

class ParticipantSkillAdminResource(resources.ModelResource):
    class Meta:
        model = participant_skill
        exclude = ('id',)        

class ParticipantAwareAdminResource(resources.ModelResource):
    class Meta:
        model = participant_aware
        exclude = ('id',)          

class ParticipantCapacAdminResource(resources.ModelResource):
    class Meta:
        model = participant_capac
        exclude = ('id',)     

class PlacementSkillAdminResource(resources.ModelResource):
    class Meta:
        model = placement_skill
        exclude = ('id',)                  