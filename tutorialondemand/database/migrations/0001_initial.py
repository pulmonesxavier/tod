# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Opentok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, 'answered'), (1, 'unanswered'), (2, 'pending')], default=1, max_length=11)),
                ('text', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, 'answered'), (1, 'unanswered'), (2, 'pending')], default=1, max_length=11)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RequestAns', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RequestAns', to='database.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='database.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_student', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_tutor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
