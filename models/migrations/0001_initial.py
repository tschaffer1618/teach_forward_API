# Generated by Django 3.0 on 2019-12-18 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User_courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('current_playtime', models.CharField(max_length=10)),
                ('is_favorite', models.BooleanField(default=False)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_in_progress', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Courses')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Users')),
            ],
        ),
        migrations.CreateModel(
            name='User_badges_courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('badge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Badges')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Courses')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Users')),
            ],
        ),
    ]
