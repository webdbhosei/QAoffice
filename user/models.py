from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Subject Master
class Subject(models.Model):
    class Meta:
        verbose_name = 'Subject Master'
        verbose_name_plural = '科目マスター'
        db_table = 'subject'

    title = models.CharField(verbose_name='科目名', max_length=50, default='')

    def __str__(self):
        return 'ID:' + str(self.id) + ', ' + self.title
