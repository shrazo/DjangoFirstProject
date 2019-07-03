from django import forms
from .models import Topic, Contact


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':'What is on your mind?'}
        ), 
        max_length=4000,
        help_text='The max length id the text is 4000',
    )
    class Meta:
        model = Topic
        fields = ['subject', 'message']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'message']
