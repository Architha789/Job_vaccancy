from django.contrib.auth.models import User  
from django import forms
from django.contrib.auth.forms import UserCreationForm  
class LoginForm(UserCreationForm):  
    class Meta:
         model=User
         fields=['username', 'email', 'password1', 'password2']
         widgets = {
          'username': forms.TextInput(attrs={'autocomplete': 'off'}),
                    }
class JobApplicationForm(forms.Form):
    cover_letter = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
