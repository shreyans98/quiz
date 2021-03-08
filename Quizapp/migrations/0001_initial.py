# Generated by Django 3.0.6 on 2020-08-22 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', max_length=200)),
                ('option1', models.CharField(default='', max_length=50)),
                ('option2', models.CharField(default='', max_length=50)),
                ('option3', models.CharField(default='', max_length=50)),
                ('option4', models.CharField(default='', max_length=50)),
                ('answer', models.CharField(default='', max_length=50)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizapp.Exam')),
            ],
        ),
    ]
