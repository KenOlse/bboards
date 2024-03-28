# Generated by Django 5.0.3 on 2024-03-27 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_advuser_first_name_alter_advuser_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Назва')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Послідовність')),
            ],
        ),
        migrations.CreateModel(
            name='SubRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Подрубрика',
                'verbose_name_plural': 'Подрубрики',
                'ordering': ('super_rubric__order', 'super_rubric__name', 'order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
        ),
        migrations.CreateModel(
            name='SuperRubric',
            fields=[
            ],
            options={
                'verbose_name': 'Надрубрика',
                'verbose_name_plural': 'Надрубрики',
                'ordering': ('order', 'name'),
                'proxy': (True,),
                'indexes': [],
                'constraints': [],
            },
            bases=('main.rubric',),
        ),
        migrations.AddField(
            model_name='rubric',
            name='super_rubric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.superrubric', verbose_name='Надрубрика'),
        ),
    ]