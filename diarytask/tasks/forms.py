from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'task', 'language']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'task': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['upload']


class AddTask(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['task']
        
