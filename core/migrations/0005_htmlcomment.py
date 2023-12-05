# Generated by Django 4.2.6 on 2023-12-03 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_dj'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('html_css', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='HTMLCOMMENT', to='core.html_css')),
            ],
        ),
    ]
