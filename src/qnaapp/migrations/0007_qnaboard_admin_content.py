# Generated by Django 3.1 on 2020-09-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnaapp', '0006_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='qnaboard',
            name='admin_content',
            field=models.TextField(null=True),
        ),
    ]