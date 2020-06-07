from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'questions', views.QuestionViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('question/POST', views.post_question,name="post-question"),
    path('question/GET', views.QuestionList.as_view(),name="questions"),
    path('question/<int:pk>/PUT', views.update_question, name="update-question"),
    # path('questions',views.questions, name='questions'),
]