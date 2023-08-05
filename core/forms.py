from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *

INPUT_CLASSES = "text-blue-500 w-[20rem] p-2 xl:p-2 rounded-xl mt-3"

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))


class CreateHTMLForm(forms.ModelForm):
    class Meta:
        model = HTMLVideo
        fields = ('title', 'video', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'video': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
            })
        }

class UpdateHTMLForm(forms.ModelForm):
    class Meta:
        model = HTMLVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }


class DeleteHTMLForm(forms.ModelForm):
    class Meta:
        model = HTMLVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }

class CreateTWCSSForm(forms.ModelForm):
    class Meta:
        model = TailwindcssVideo
        fields = ('title', 'video', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'video': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
            })
        }

class UpdateTWCSSForm(forms.ModelForm):
    class Meta:
        model = TailwindcssVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }


class DeleteTWCSSForm(forms.ModelForm):
    class Meta:
        model = TailwindcssVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }

class CreatePyForm(forms.ModelForm):
    class Meta:
        model = PythonVideo
        fields = ('title', 'video', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'video': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
            })
        }

class UpdatePyForm(forms.ModelForm):
    class Meta:
        model = PythonVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }


class DeletePyForm(forms.ModelForm):
    class Meta:
        model = PythonVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }

class CreateDjForm(forms.ModelForm):
    class Meta:
        model = DjangoVideo
        fields = ('title', 'video', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'video': forms.TextInput(attrs={
                'class': ' p-2 w-[19rem] rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
            })
        }

class UpdateDjForm(forms.ModelForm):
    class Meta:
        model = DjangoVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }


class DeleteDjForm(forms.ModelForm):
    class Meta:
        model = DjangoVideo
        fields = ('title', 'video', 'description',)
        widgets = {
        'title': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'video': forms.TextInput(attrs={
            'class': ' p-2 w-[19rem] rounded-xl'
        }),
        'description': forms.TextInput(attrs={
            'class': ' p-1 mb-5 h-[5rem] w-[19rem] rounded-xl'
        })
    }

class DeleteAcctForm(forms.ModelForm):
    pass

class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))