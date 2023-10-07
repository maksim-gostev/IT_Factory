from rest_framework import serializers

from a_store.models import A_Stores


class A_StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = A_Stores
        exclude = ('worker',)
