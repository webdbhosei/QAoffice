from django import forms
from post.models import Question

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['content','title']
  
  content = forms.CharField(
    label="Content",
    widget=forms.TextArea(attrs={'id':"QuestionContent",'placeholder'="質問内容を入力してください。"})
  )

  subject = forms.CharField(
    label="Subject",
    widget=forms.TextInput(attrs={'id':"QuestionSubject",'placeholder':"科目"})
  )