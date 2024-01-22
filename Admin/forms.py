from django import forms
from .models import Job
class adminform(forms.ModelForm):

    class  Meta:
        model = Job
        fields = '__all__'