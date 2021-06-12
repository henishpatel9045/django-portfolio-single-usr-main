from django.forms import boundfield, fields, widgets
from .models import Comment
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, widget=widgets.TextInput(attrs={'class':'form-control', 'style':"width: 100%", "placeholder": "Name"}))
    email = forms.EmailField(widget=widgets.EmailInput(attrs={'class':'form-control', 'style':"width: 100%", "placeholder": "Email"}))
    body = forms.CharField(widget=widgets.Textarea(attrs={'class':'form-control', 'rows':5, 'columns':30, 'style':"width: 100%", "placeholder": "Body"}))
    
