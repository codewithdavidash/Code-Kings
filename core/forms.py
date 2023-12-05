from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm,
    AuthenticationForm
)
from django import forms
from .models import *


COMMENT_CLASS = """
border border-gray-500 p-2 rounded-xl w-[100%]
"""
AUTH_VIEWS = """
border-b text-rose-900 border-rose-900  w-[17rem] lg:w-[20rem] bg-transparent
"""
HTML_CSS_TITLE_CLASS = """
    border-b border-red-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
HTML_CSS_YOUTUBE_SOURCE_CLASS = """
    border-b border-red-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
HTML_CSS_DETAILS_CLASS = """
    border-gray-300 border bg-white  w-[17rem] lg:w-[20rem] lg:h-[5rem] bg-transparent
"""
JS_TITLE_CLASS = """
    border-b border-yellow-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
JS_YOUTUBE_SOURCE_CLASS = """
    border-b border-yellow-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
JS_DETAILS_CLASS = """
    border-gray-300 border bg-white  w-[17rem] lg:w-[20rem] lg:h-[5rem] bg-transparent
"""
PY_TITLE_CLASS = """
    border-b border-blue-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
PY_YOUTUBE_SOURCE_CLASS = """
    border-b border-blue-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
PY_DETAILS_CLASS = """
    border-gray-300 border bg-white  w-[17rem] lg:w-[20rem] lg:h-[5rem] bg-transparent
"""
DJ_TITLE_CLASS = """
    border-b border-green-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
DJ_YOUTUBE_SOURCE_CLASS = """
    border-b border-green-500  w-[17rem] lg:w-[20rem] bg-transparent bg-transparent
"""
DJ_DETAILS_CLASS = """
    border-gray-300 border bg-white  w-[17rem] lg:w-[20rem] lg:h-[5rem] bg-transparent
"""


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email','password1', 'password2']
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': AUTH_VIEWS
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': AUTH_VIEWS
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': AUTH_VIEWS
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': AUTH_VIEWS
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": AUTH_VIEWS
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))


class ADDHTMLCSSVIDS(forms.ModelForm):
    class Meta:
        model = HTML_CSS
        fields = ('title', 'youtube_source', 'pdf', 'details',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': HTML_CSS_TITLE_CLASS
            }),
            'youtube_source': forms.URLInput(attrs={
                'class': HTML_CSS_YOUTUBE_SOURCE_CLASS
            }),
            'pdf': forms.FileInput(attrs={
                'class': HTML_CSS_YOUTUBE_SOURCE_CLASS
            }),
            'details': forms.Textarea(attrs={
                'class': HTML_CSS_DETAILS_CLASS
            }),
        }
        
class JSVIDS(forms.ModelForm):
    class Meta:
        model = JS
        fields = ('title', 'youtube_source', 'pdf', 'details',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': JS_TITLE_CLASS
            }),
            'youtube_source': forms.URLInput(attrs={
                'class': JS_YOUTUBE_SOURCE_CLASS
            }),
            'pdf': forms.FileInput(attrs={
                'class': JS_TITLE_CLASS
            }),
            'details': forms.Textarea(attrs={
                'class': JS_DETAILS_CLASS
            }),
        }
        
class PYVIDS(forms.ModelForm):
    class Meta:
        model = PY
        fields = ('title', 'youtube_source', 'pdf', 'details',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': PY_TITLE_CLASS
            }),
            'youtube_source': forms.URLInput(attrs={
                'class': PY_YOUTUBE_SOURCE_CLASS
            }),
            'pdf': forms.FileInput(attrs={
                'class': PY_TITLE_CLASS
            }),
            'details': forms.Textarea(attrs={
                'class': PY_DETAILS_CLASS
            }),
        }
       
        
class DJVIDS(forms.ModelForm):
    class Meta:
        model = DJ
        fields = ('title', 'youtube_source', 'pdf', 'details',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': DJ_TITLE_CLASS
            }),
            'youtube_source': forms.URLInput(attrs={
                'class': DJ_YOUTUBE_SOURCE_CLASS
            }),
            'pdf': forms.FileInput(attrs={
                'class': DJ_TITLE_CLASS
            }),
            'details': forms.Textarea(attrs={
                'class': DJ_DETAILS_CLASS
            }),
        }
        
#   Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={
                'class': COMMENT_CLASS,
                'placeholder': 'Say Something...',
                'autofocus': 'True',
            }),
        }
     
        
#   Password Change Forms
class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": AUTH_VIEWS
    }))
