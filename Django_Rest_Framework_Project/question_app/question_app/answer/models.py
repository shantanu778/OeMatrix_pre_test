from django.db import models
from ..question.models import Question
from django.contrib.auth.models import User 

# Create your models here.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="ques_answer")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_answer")
    name = models.CharField(max_length=5)
    def __str__(self):
        return self.name
