from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from post.models import Question, Answer


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
    queryset = Question.objects.all()
    template_name = "post/question_list.html"
    success_url = "post:list_question"

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


class QuestionCreateView(generic.CreateView):
    model = Question
    template_name = "entry/KY/KY_0141.html"
    success_url = "post:list_question"
    fields = ['content','subject']
    object = None

    def form_valid(self, form):
        self.object=form.save(commit=False)
        # self.object.questioner="Someone"
        self.object.save()

        return redirect('post:list_question')


class QuestionUpdateView(generic.UpdateView):
    model = Question
    template_name = "entry/KY/KY_0141.html"
    success_url = "post:list_question"
    fields = ['content', 'subject']
    object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return redirect('post:list_question')



# ToDo: classes to register Answers
# -- Assigned to Tao-san
class AnswerListView(generic.ListView):
    model = Answer


class AnswerCreateView(generic.CreateView):
    model = Answer


class AnswerUpdateView(generic.UpdateView):
    model = Answer
