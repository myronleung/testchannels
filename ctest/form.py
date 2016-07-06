from django import forms

class MessageForm(forms.Form):
    author = forms.CharField(label = 'username', max_length=20)
    message = forms.TextField(label = 'message')
