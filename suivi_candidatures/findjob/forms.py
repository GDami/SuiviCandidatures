from django import forms
from findjob.models import Application, Company, Callback

class AddApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        # fields = '__all__'
        exclude = ("called_back","callback")

class AddCallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        #exclude = ('title",)