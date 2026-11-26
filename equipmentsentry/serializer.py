from rest_framework import serializers
from equipmentsentry.models import EquipmentEntry

class EquipmentEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentEntry
        fields = '__all__'