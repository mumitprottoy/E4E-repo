# Generated by Django 5.0.6 on 2024-07-16 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0005_university_alter_question_meta'),
        ('tests', '0003_alter_testquestion_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='marking_criterion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tests.markingcriterion'),
        ),
        migrations.AlterField(
            model_name='markingcriterion',
            name='name',
            field=models.CharField(default='MC__1_0__0_25__0_0', max_length=20),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qb.question'),
        ),
    ]
