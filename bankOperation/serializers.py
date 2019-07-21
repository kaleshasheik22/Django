from rest_framework import serializers
from . import models


class bankSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.banks


class branchSerializer(serializers.ModelSerializer):

    class Meta:
         fields = '__all__'
         model = models.branches