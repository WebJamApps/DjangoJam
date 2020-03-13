from rest_framework import serializers

from .models import Tutorial


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('tutorial_title', 'tutorial_content', 'tutorial_published')
