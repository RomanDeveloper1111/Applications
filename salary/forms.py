from django import forms
from .models import *


class AddFineForm(forms.ModelForm):
    name = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': '3'}), label='Наименование')
    note = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows': '4'}), label='Примечание')
    cost = forms.DecimalField(widget=forms.widgets.TextInput(attrs={'type': 'number', 'class': 'form-control fl'}),
                              label='Стоимость')
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(),
                                    widget=forms.widgets.Select(attrs=
                                                                   {'class': 'form-control fl'}),
                                    label='Работник')

    class Meta:
        model = Fine
        fields = ('name', 'cost', 'worker', 'note',)


class EditEmploy(forms.ModelForm):

    class Meta:
        model = Worker
        fields = '__all__'


class NewPosition(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'


class AddNewWorker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('first_name', 'second_name', 'position')
