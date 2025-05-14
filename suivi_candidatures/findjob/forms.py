from django import forms
from findjob.models import Application, Company, Callback

class AddApplicationForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.order_by('name'))

    class Meta:
        model = Application
        # fields = '__all__'
        exclude = ("called_back", "callback", "state")

class AddCallbackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        #exclude = ('title",)