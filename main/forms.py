from django import forms
from .models import Batalla

class BatallaForm(forms.ModelForm):
    class Meta:
        model = Batalla
        fields = ['spider_man', 'enemigo', 'fecha', 'resultado']