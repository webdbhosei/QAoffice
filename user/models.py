from django.db import models
from django.contrib.auth.models import Group, User as MyUser
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


# Student Master
class Student(models.Model):
    class Meta:
        verbose_name = 'Student Master'
        verbose_name_plural = '学生マスター'
        db_table = 'student'

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    is_ta = models.BooleanField(verbose_name='is TA', default=False)
    number = models.CharField(verbose_name='学生証番号', max_length=12, default='')

    def __str__(self):
        return 'ID:' + str(self.id) + ', 学生証番号:' + str(self.number) + \
               ', e-mail:' + self.user.email + ', name:' + \
               self.user.first_name + self.user.last_name


# Register Student when admin created user instance
@receiver(post_save, sender=MyUser)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


# Update by synchronizing with MyUser model
@receiver(post_save, sender=MyUser)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()


# Teacher Master
class Teacher(models.Model):
    class Meta:
        verbose_name = 'Teacher Master'
        verbose_name_plural = '教員マスター'
        db_table = 'teacher'

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return 'ID:' + str(self.id) + ', name:' + \
               self.user.first_name + self.user.last_name


# Register Teacher when admin created user instance
@receiver(post_save, sender=MyUser)
def create_user_teacher(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.create(user=instance)


# Update by synchronizing with MyUser model
@receiver(post_save, sender=MyUser)
def save_user_teacher(sender, instance, **kwargs):
    instance.teacher.save()
