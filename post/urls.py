from django.urls import path

from post.views import QuestionListView, index

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('questions', QuestionListView.as_view(), name='list_question'),
    path('questions/<str:tag>/', QuestionListView.as_view(), name="tag_list_question"),
]
