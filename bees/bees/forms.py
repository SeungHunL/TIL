from django.forms.widgets import Textarea
from .models import Bee
from django import forms
 
class BeeForm(forms.ModelForm):
    name = forms.CharField(
        label='NAME',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the name',
            }
        ),
    )
    content = forms.CharField(
        label='CHARACTERISTIC',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the characteristic',
                'row':5,
                'col':15,
            }
        ),
        error_messages={
            'required':'Please enter your content'
        }
    )
    class Meta:
        model = Bee
        fields = '__all__'
    