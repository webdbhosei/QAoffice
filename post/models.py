from django.db import models

from django.contrib.auth.models import Group, User as MyUser
from user.models import Subject


# Question Table
class Question(models.Model):
    class Meta:
        verbose_name = 'Question Table'
        verbose_name_plural = '質問テーブル'
        db_table = 'question'

    subject = models.ForeignKey(Subject, verbose_name='科目', on_delete=models.SET_NULL, null=True)
    questioner = models.ForeignKey(MyUser, verbose_name='質問者', on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name='質問内容', max_length=1000, default='',blank=True)


# Answer Table2020/7/7(Tue)

class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer Table'
        verbose_name_plural = '回答テーブル'
        db_table = 'answer'

    question = models.ForeignKey(Question, verbose_name='質問', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='回答内容', max_length=1000, default='')
    answerer = models.ForeignKey(MyUser, verbose_name='回答者', on_delete=models.SET_NULL, null=True)

