# Generated by Django 4.1 on 2022-08-16 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycontent', '0003_alter_commentmodel_answer_alter_commentmodel_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answermodel',
            old_name='body',
            new_name='abody',
        ),
        migrations.RenameField(
            model_name='commentmodel',
            old_name='body',
            new_name='cbody',
        ),
    ]
