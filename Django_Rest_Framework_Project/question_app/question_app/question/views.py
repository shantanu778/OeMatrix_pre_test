from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import QuestionSerializer
from .models import Question
# Create your views here.

@permission_classes((IsAuthenticated,IsAdminUser))
class QuestionList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        questions = Question.objects.all().order_by("id")
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)



# class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


# class QuestionDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Question.objects.get(pk=pk)
#         except Question.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST',])
@permission_classes((IsAuthenticated,IsAdminUser))
def post_question(request):
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT',])
@permission_classes((IsAuthenticated,IsAdminUser))
def update_question(request,pk):
    try:
        question = Question.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data= request.data)
        data ={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successfully"
            return Response(data = data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)