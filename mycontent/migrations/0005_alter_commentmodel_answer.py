# Generated by Django 4.1 on 2022-08-16 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycontent', '0004_rename_body_answermodel_abody_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_comment', to='mycontent.answermodel'),
        ),
    ]