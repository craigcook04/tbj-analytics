from django import forms

class searchForm(forms.Form):
    searchForm = forms.CharField(label='Search Team: ', max_length=100)