from django.db import models

# Create your models here.

# create subjects model
class Subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

#create questions model
class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=500)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)

