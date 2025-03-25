from django import forms
from .models import ActualTask

class TaskFormCreate(forms.ModelForm):
    class Meta:
        model = ActualTask
        fields = ['task_title', 'task_description', 'task_due_date', 'task_status',
                   'task_priority', 'task_category']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'task_due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'task_status': forms.Select(attrs={'class': 'form-select'}),
            'task_priority': forms.Select(attrs={'class': 'form-select'}),
            'task_category': forms.Select(attrs={'class': 'form-select'}),
        }

        
