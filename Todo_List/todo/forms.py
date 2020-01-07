import datetime

from django import forms
from .models import TodoList


class CreateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={"placeholder" : "YYYY-MM-DD"}))
    task = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Task"}))

    class Meta:
        model = TodoList
        fields = [
            'date',
            'task',
        ]

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

