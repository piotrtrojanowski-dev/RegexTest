from django.forms import ModelForm, Textarea
from . import models


class TestForm(ModelForm):

    class Meta:
        model = models.Regex
        fields = '__all__'
        widgets = {'text': Textarea(attrs={'rows': 10, 'cols': 80})}