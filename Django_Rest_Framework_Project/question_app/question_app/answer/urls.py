from django.urls import path, include
from . import views



urlpatterns = [
    # path('', include(router.urls)),
    path('POST', views.save_answer,name="save-answer"),
    path('GET', views.AnswersList.as_view(),name="get-answer"),
    #path('question/<int:pk>/PUT', views.update_question, name="update-question"),
    #path('questions',views.questions, name='questions'),
]