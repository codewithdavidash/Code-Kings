from django.contrib.auth.models import User
from django.db import models


class HTMLVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class PythonVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class TailwindcssVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class DjangoVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title