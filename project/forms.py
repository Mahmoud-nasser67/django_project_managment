from django import forms
from .models import Progect
attrs={'class': 'form-control'}
class project_forms(forms.ModelForm):

    class Meta:

        model=Progect
        fields = ['title', 'description', 'category']
        widgets= {
            'title':forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs),
            'category':forms.Select(attrs=attrs),
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Progect
        fields = ['title', 'description', 'category','statues']

        widgets = {
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs),
            'category': forms.Select(attrs=attrs),
            'statues': forms.Select(attrs=attrs),
        }