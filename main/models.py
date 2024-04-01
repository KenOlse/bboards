from django.db import models
from django.contrib.auth.models import AbstractUser

from .utilities import get_timestamp_path


class AdvUser(AbstractUser):
    """docstring for AdvUser"""

    is_activated = models.BooleanField(default=True,
                                       db_index=True, verbose_name='Актівацію пройдено')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Присилати сповіщення щодо коментарів')

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

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
        return '%s - %s' % (self.super_rubric.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_rubric__order',
                    'super_rubric__name', 'order', 'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'


class Bb(models.Model):
    rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT,
                               verbose_name='Рубрика')
    title = models.CharField('Товар', max_length=40)
    content = models.TextField('Опис')
    price = models.FloatField(default=0, verbose_name='Ціна')
    contacts = models.TextField(verbose_name='Контакти')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path,
                              verbose_name='Зображення')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
                               verbose_name='Автор об`яви')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Виводити до списку?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубліковано')

    def delete(self, *args, **kwargs):
        for ai in self.additionlimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Об`ва'
        verbose_name_plural = 'Об`яви'
        ordering = ('-created_at',)


class AdditionalImage(models.Model):
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE,
                           verbose_name='Об`ява')
    image = models.ImageField(upload_to=get_timestamp_path,
                              verbose_name='Зображення')

    class Meta:
        verbose_name = 'Додаткова іллюстрація'
        verbose_name_plural = 'Додаткові іллюстрації'
