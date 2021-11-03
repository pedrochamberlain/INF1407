from django import forms
from movies.models import Filme


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
