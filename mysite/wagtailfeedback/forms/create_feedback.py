from django import forms
from blog.models import Feedback
from django.core.exceptions import ValidationError

class FeedbackcreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Feedback
        fields = [
            'date', 'title', 'texto'
        ]
        error_messages = {
            'title':{
                'required':'O feedback precisa ter um título',
                'invalid':'O feedback precisa ter um título'
            },
            'texto':{
                'required':'O feedback precisa ter uma descrição',
                'invalid':'O feedback precisa ter uma descrição'
            }
        }
        widgets = {
            'date':forms.DateField(
                widget=forms.DateInput(
                    format='%d/%m/%Y',
                    attrs={
                        'id_for_label':'Data'
                    }
                ),
                label='Data'
            )
        }
    
    def clean_title(self):
        data = self.cleaned_data.get('title')

        if len(data) > 0:
            return data
        
        return ValidationError('O feedback precisa ter um título', code='invalid')

    def clean_texto(self):
        data = self.cleaned_data.get('texto')

        if len(data) > 0:
            return data
        
        return ValidationError(
            'O feedback precisa ter uma descrição', code='invalid'
        )
