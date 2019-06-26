from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'What is on your mind?'
        }),
        max_length=4000,
        help_text='The max length of the text id 4000.')
    special_comment = forms.CharField(max_length=200, )

    class Meta:
        model = Topic
        fields = ['subject', 'message', 'special_comment']


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=200,
        help_text='The max length of the text id 4000.',
        widget=forms.Textarea(attrs={'placeholder': 'Full name'}))
    email = forms.EmailField(widget=forms.Textarea(
        attrs={'placeholder': 'E-mail Address'}))
    phone = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Phone Number'}),
        help_text='e.g. +8801737520527')
    message = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
