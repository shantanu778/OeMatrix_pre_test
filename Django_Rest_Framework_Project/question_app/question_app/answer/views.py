from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializer import AnswerSerializer, AnswerPostSerializer
from ..question.models import Question
from .models import Answer

# Create your views here.
@permission_classes((IsAuthenticated,))
class AnswersList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        answers = Answer.objects.all().order_by("id")
        
        if not request.user.is_superuser:
            answers = Answer.objects.filter(user = request.user).order_by("id")

        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def save_answer(request):
    if request.method == 'POST':
        data = {}
        try:
            question = Question.objects.get(pk = request.data['question'])
        except Exception as e:
            print(e)
        serializer = AnswerPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user, question = question)
            data['response'] = "Answer received Successfully"
        else:
            data = serializer.errors
        return Response(data)