# Generated by Django 4.2.6 on 2023-12-03 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_htmlcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlcomment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PYComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user3', to=settings.AUTH_USER_MODEL)),
                ('py', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PYCOMMENT', to='core.py')),
            ],
        ),
        migrations.CreateModel(
            name='JSComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
                ('js', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='JSCOMMENT', to='core.js')),
            ],
        ),
        migrations.CreateModel(
            name='DJComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user4', to=settings.AUTH_USER_MODEL)),
                ('dj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DJCOMMENT', to='core.dj')),
            ],
        ),
    ]