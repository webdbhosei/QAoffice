from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from django.contrib import messages
from django.db.models import Q

from functools import reduce
from operator import and_

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
    template_name = "post/question_list.html"
    success_url = "post:list_question"

    def get_queryset(self):
        queryset = Question.objects.all()
        keyword = self.request.GET.get('keyword')

        if keyword:
            q_word = self.request.GET.get('keyword')
            q_list = q_word.split()
            queryset = Question.objects.filter(tag__name__in=q_list)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

        return queryset

    # ListView has 'object_list' default attribute, and it is set
    # by default.  However, it will select all questions.
    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return render(request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super(QuestionListView, self).get_context_data(**kwargs)
    #     chosen_question = Question.objects.filter(something=something)
    #     context.update(
    #        {'object_list': chosen_question},
    #     )
    #     return context

#
# class QuestionListView(generic.ListView):
#     model = Question
#
#     def get_context_data(self, **kwargs):
#         context = super(QuestionListView, self).get_context_data(**kwargs)
#         return context


class TagListView(generic.ListView):
    model = Question
    template_name = "post/question_list.html"

    def get_queryset(self):
        queryset = Question.objects.filter(tag__name=self.kwargs['tag'])
        return queryset


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
