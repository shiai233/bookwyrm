# Generated by Django 3.2.12 on 2022-03-04 23:19

import bookwyrm.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0146_alter_user_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='question',
            field=bookwyrm.models.fields.TextField(blank=True, max_length=500),
        ),
    ]
