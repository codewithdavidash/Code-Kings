# Generated by Django 4.2.6 on 2023-12-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_comment_remove_htmlcomment_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=255),
        ),
    ]