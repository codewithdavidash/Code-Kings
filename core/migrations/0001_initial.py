# Generated by Django 4.2.6 on 2023-11-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HTML_CSS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('youtube_source', models.URLField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='static/images/')),
                ('details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'HTML AND CSS',
                'verbose_name_plural': 'HTML AND CSS',
                'ordering': ('-created_at',),
            },
        ),
    ]
