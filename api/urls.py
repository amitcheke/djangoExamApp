from django.contrib import admin
from django.urls import include, path
from api.views import QuestionViewSet, SubjectViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
