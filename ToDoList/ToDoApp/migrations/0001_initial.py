# Generated by Django 4.1.3 on 2022-11-13 22:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('is_payment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32)),
                ('sign_up_date', models.DateField(default=datetime.date.today)),
                ('nickname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('can_create_task', models.BooleanField(default=False)),
                ('can_finish_task', models.BooleanField(default=False)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('is_important', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('completion_time', models.DateTimeField(blank=True, default=datetime.date.today, null=True)),
                ('completion_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.category')),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_completed_by_user', to='ToDoApp.user')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created_by_user', to='ToDoApp.user')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='creator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDoApp.user'),
        ),
        migrations.AddField(
            model_name='category',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_in_room', to='ToDoApp.room'),
        ),
    ]
