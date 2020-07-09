from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Question, Answer


def index(request):
    return HttpResponse("Welcome to QA Office.<br/>"
                        "This is the page to manage posts.<br />"
                        "Empty Now.")


# ToDo: Here should be a method to the List of Questions
# -- Assigned to Yamamoto-san
#  <----- Nomura-san's idea will be installed in this class.
#  <----- Searching Logic will be installed here: Uemura-san, and Kobayashi-san
class QuestionListView(generic.ListView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        return context


class QuestionCreateView(generic.CreateView):
    model = Question


class QuestionUpdateView(generic.UpdateView):
    model = Question


# ToDo: classes to register Answers
# -- Assigned to Tao-san
class AnswerListView(generic.ListView):
    model = Answer


class AnswerCreateView(generic.CreateView):
    model = Answer


class AnswerUpdateView(generic.UpdateView):
    model = Answer
