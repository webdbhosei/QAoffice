from django import forms
from post.models import Question

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['']