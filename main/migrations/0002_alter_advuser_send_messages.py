# Generated by Django 5.0.3 on 2024-03-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='send_messages',
            field=models.BooleanField(default=True, verbose_name='Присилати сповіщення щодо коментарів'),
        ),
    ]
