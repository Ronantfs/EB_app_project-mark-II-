# Generated by Django 4.1.1 on 2022-09-15 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EB_app', '0002_question_tags_alter_question_as_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_progress',
            field=models.IntegerField(default=0),
        ),
    ]