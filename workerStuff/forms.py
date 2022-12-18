from django import forms
from .models import *


class AskForm(forms.ModelForm):
    fio = forms.CharField(label="Имя сотрудника")

    class Meta:
        model = Requests
        fields = ['theme', 'description_of_problem', 'fio']
        widgets = {
            'description_of_problem': forms.Textarea(attrs={'cols': 10, 'rows': 4}),
            'fio': forms.TextInput(attrs={'type': 'hidden'})
        }

    def save(self, commit=True):
        if commit is True:
            self.cleaned_data.pop("fio")
            print(self.cleaned_data)
        return super(AskForm, self).save(commit=commit)
