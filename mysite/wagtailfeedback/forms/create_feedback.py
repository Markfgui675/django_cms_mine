from django import forms
from blog.models import Feedback
from django.core.exceptions import ValidationError
from datetime import date

class FeedbackcreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    date = forms.DateField(
        initial=date.today,
        label='Data',
        widget=forms.TextInput(
            attrs={
                'class':'slug_hide',
                'type':'date',
            }
        )
    )

    slug = forms.CharField(
        required=False,
        label='Slug',
        widget=forms.TextInput(
            attrs={
                'class':'slug_hide',
                'type':'text',
                'value':''
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ['date', 'title', 'texto', 'slug']
        error_messages = {
            'data':{
                'invalid':'Inválido'
            },
            'title':{
                'required':'O feedback precisa ter um título',
                'invalid':'O feedback precisa ter um título'
            },
            'texto':{
                'required':'O feedback precisa ter uma descrição',
                'invalid':'O feedback precisa ter uma descrição'
            }
        }

    def clean_title(self):
        data = self.cleaned_data.get('title')

        if len(data) <= 2:
            raise ValidationError('O feedback precisa ter um título', code='invalid')

        return data

    def clean_texto(self):
        data = self.cleaned_data.get('texto')

        if len(data) < 0:
            raise ValidationError(
            'O feedback precisa ter uma descrição', code='invalid'
        )

        return data   

    def clean_date(self):
        data = self.cleaned_data.get('date')
        return data
    