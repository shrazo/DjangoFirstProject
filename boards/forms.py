from django import forms
from .models import Topic, Contact


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)
    description = forms.CharField(widget=forms.Textarea(), max_length=2000)

    class Meta:
        model = Topic
        fields = ['subject', 'message', 'description']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'message']
