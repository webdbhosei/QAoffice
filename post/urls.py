from django.urls import path

from post.views import QuestionListView, index, QuestionCreateView

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('questions', QuestionListView.as_view(), name='list_question'),
    path('question', QuestionCreateView.as_view(), name='post_question'),
]
