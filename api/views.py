from django.shortcuts import render
from rest_framework import viewsets
from api.models import Question, Subject
from api.serializers import QuestionSerializers, SubjectSeriallizer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializers

class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSeriallizer