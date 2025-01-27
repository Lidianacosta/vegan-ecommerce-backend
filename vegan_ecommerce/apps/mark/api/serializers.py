from rest_framework import serializers

from apps.mark.models import Mark


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = ('id', 'name', 'slug')
