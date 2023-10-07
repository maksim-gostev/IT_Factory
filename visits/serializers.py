from rest_framework import serializers

from visits.models import Visits


class VisitingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visits
        fields = ('id', 'data')