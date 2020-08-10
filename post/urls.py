from django.urls import path

from post.views import QuestionListView, index, QuestionCreateView, QuestionUpdateView

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('questions', QuestionListView.as_view(), name='list_question'),
    path('question_new', QuestionCreateView.as_view(), name='create_question'),
    path('question_edit/<int:pk>', QuestionUpdateView.as_view(), name='edit_question'),
]
