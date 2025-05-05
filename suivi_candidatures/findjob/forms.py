from django import forms
from findjob.models import Application, Company

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        #exclude = ('title",)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        #exclude = ('title",)