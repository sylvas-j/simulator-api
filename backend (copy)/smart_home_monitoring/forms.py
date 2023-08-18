from django import forms
from smart_home_monitoring.models import UploadData
from django.contrib.auth.models import User




class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UploadData
        fields = '__all__'
        exclude = ['reg_date','pred_range']
        
        widgets = {
            # 'pred_range'  :   forms.TextInput(attrs={'class':'form-control'}),
            'excel_file'  :   forms.FileInput(attrs={'class':'form-control'}),
            
        }

