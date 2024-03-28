from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """docstring for AdvUser"""

    is_activated = models.BooleanField(default=True,
                                       db_index=True, verbose_name='Актівацію пройдено')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Присилати сповіщення щодо коментарів')

    class Meta(AbstractUser.Meta):
        pass


class Rubric(models.Model):
    name = models.CharField('Назва', max_length=20, db_index=True, unique=True)
    order = models.SmallIntegerField('Послідовність', default=0, db_index=True)
    super_rubric = models.ForeignKey('SuperRubric',
                                     on_delete=models.PROTECT, null=True, blank=True, verbose_name='Надрубрика')


class SuperRubricManager(models.Manager):
    def get_queryset(selt):
        return super().get_queryset().filter(super_rubric__isnull=True)


class SuperRubric(Rubric):
    objects = SuperRubricManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True,
        ordering = ('order', 'name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'



class SubRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=False)


class SubRubric(Rubric):
    objects = SubRubricManager()

    def __str__(self):
        return '%s - %s' % (self.super.super_rubric.name, self.name)


    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'