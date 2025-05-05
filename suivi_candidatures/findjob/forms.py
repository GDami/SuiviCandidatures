from django import forms
from findjob.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        #exclude = ('title",)