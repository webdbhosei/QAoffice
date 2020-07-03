from django.db import models

from user.models import Subject, Student, Teacher


# Question Table
class Question(models.Model):
    class Meta:
        verbose_name = 'Question Table'
        verbose_name_plural = '質問テーブル'
        db_table = 'question'

    subject = models.ForeignKey(Subject, verbose_name='科目', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, verbose_name='質問者', on_delete=models.SET_NULL, null=True)
    content = models.CharField(verbose_name='質問内容', max_length=1000, default='')


# Answer Table
class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer Table'
        verbose_name_plural = '回答テーブル'
        db_table = 'answer'

    question = models.ForeignKey(Question, verbose_name='質問', on_delete=models.CASCADE)
    content = models.CharField(verbose_name='回答内容', max_length=1000, default='')
    teacher = models.ForeignKey(Teacher, verbose_name='回答者(教員)', on_delete=models.SET_NULL, null=True)
    ta = models.ForeignKey(Student, verbose_name='回答者(TA)', on_delete=models.SET_NULL, null=True)

