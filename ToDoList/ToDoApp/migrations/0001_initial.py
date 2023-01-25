# Generated by Django 4.1.5 on 2023-01-22 14:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_payment', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('nickname', models.CharField(max_length=30)),
                ('avatar', models.ImageField(default='/media/default-avatar/avatar1.png', upload_to='media/avatars')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField()),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_important', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('completion_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('completion_comment', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.category')),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Zadanie',
                'verbose_name_plural': 'Zadania',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('can_create_task', models.ManyToManyField(default=False, related_name='can_create_task', to=settings.AUTH_USER_MODEL)),
                ('can_finish_task', models.ManyToManyField(default=False, related_name='can_finish_task', to=settings.AUTH_USER_MODEL)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('is_moderator', models.ManyToManyField(default=False, related_name='is_moderator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pokój',
                'verbose_name_plural': 'Pokoje',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.room'),
        ),
    ]
