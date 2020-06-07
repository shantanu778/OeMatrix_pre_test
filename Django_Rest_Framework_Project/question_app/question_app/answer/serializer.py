from rest_framework import serializers
from .models import Answer
from ..question.models import Question
from django.contrib.auth.models import User

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):    
    ques_answer = AnswerSerializer(many=True, read_only=True)      
    class Meta:        
        model = Question         
        fields = ("name","ques_answer",)

class UserSerializer(serializers.ModelSerializer):    
    user_answer = AnswerSerializer(many=True, read_only=True)      
    class Meta:        
        model = User         
        fields = ("name","user_answer",)

class AnswerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('name',)

    
