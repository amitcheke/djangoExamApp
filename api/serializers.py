from rest_framework import serializers
from api.models import Question,Subject

class QuestionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Question
        fields="__all__"

class SubjectSeriallizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Subject
        fields="__all__"
        