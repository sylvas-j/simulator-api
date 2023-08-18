from django import forms
from court_cases_classification.models import UploadCourtCase
from django.contrib.auth.models import User




class UploadCourtCaseForm(forms.ModelForm):
    class Meta:
        model = UploadCourtCase
        fields = '__all__'
        exclude = ['reg_date']
        
        widgets = {
            'text'  :   forms.TextInput(attrs={'class':'form-control'}),
            'excel_file'  :   forms.FileInput(attrs={'class':'form-control'}),
            
        }
    def __init__(self, *args, **kwargs):
        super(UploadCourtCaseForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
        self.fields['excel_file'].required = False
        self.fields['sentence'].required = False
        self.fields['crime'].required = False
        


# class UploadCourtCaseForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': 40, 'rows': 20}))
#     excel_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    # comment = forms.CharField(widget=forms.Textarea)
