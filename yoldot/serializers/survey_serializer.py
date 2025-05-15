from rest_framework import serializers
from ..models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
    def to_representation(self, instance):
        """ Override default representation to use verbose_name as JSON key """
        rep = super().to_representation(instance)
        new_rep = {}
        for field in self.Meta.model._meta.fields:
            verbose_name = field.verbose_name
            new_rep[verbose_name] = rep[field.name]
        return new_rep
