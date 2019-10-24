from django import forms

from .models import Journal, Entry

class CreateJournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = '__all__'

class CreateEntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'