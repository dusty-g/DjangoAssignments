from django import forms

class noteForm(forms.Form):
    note = forms.CharField(max_length = 150, widget = forms.Textarea)