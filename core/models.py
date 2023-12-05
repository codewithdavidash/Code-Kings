from django.contrib.auth.models import User
from django.db import models


class HTML_CSS(models.Model):
    title = models.CharField(max_length=100)
    youtube_source = models.URLField()
    pdf = models.FileField(upload_to='static/files/', null=True, blank=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'HTML AND CSS VIDEOS'
        verbose_name_plural = 'HTML AND CSS VIDEOS'
        

class JS(models.Model):
    title = models.CharField(max_length=100)
    youtube_source = models.URLField()
    pdf = models.FileField(upload_to='static/files/', null=True, blank=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'JAVASCRIPT VIDEOS'
        verbose_name_plural = 'JAVASCRIPT VIDEOS'
        
class PY(models.Model):
    title = models.CharField(max_length=100)
    youtube_source = models.URLField()
    pdf = models.FileField(upload_to='static/files/', null=True, blank=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'PYTHON VIDEOS'
        verbose_name_plural = 'PYTHON VIDEOS'
        
class DJ(models.Model):
    title = models.CharField(max_length=100)
    youtube_source = models.URLField()
    pdf = models.FileField(upload_to='static/files/', null=True, blank=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'DJANGO VIDEOS'
        verbose_name_plural = 'DJANGO VIDEOS'
        
        
class Comment(models.Model):
    created_by = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.created_by.username}'
    class Meta:
        ordering = ('-created_at',)