# Generated by Django 5.0.3 on 2024-03-28 17:14

import django.db.models.deletion
import main.utilities
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rubric_subrubric_superrubric_rubric_super_rubric'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Товар')),
                ('content', models.TextField(verbose_name='Опис')),
                ('price', models.FloatField(default=0, verbose_name='Ціна')),
                ('contacts', models.TextField(verbose_name='Контакти')),
                ('image', models.ImageField(blank=True, upload_to=main.utilities.get_timestamp_path, verbose_name='Зображення')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Виводити до списку?')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор об`яви')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subrubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Об`ва',
                'verbose_name_plural': 'Об`яви',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.utilities.get_timestamp_path, verbose_name='Зображення')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bb', verbose_name='Об`ява')),
            ],
            options={
                'verbose_name': 'Додаткова іллюстрація',
                'verbose_name_plural': 'Додаткові іллюстрації',
            },
        ),
    ]
