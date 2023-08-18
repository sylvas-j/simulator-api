from django.db import models
from django.conf import settings
from django.urls import reverse



class UploadCourtCase(models.Model):

    text = models.TextField(max_length=1000, null=True)
    sentence = models.TextField(max_length=20, null=True)
    crime = models.TextField(max_length=50, null=True)
    excel_file = models.FileField(upload_to='data_files', null=True)
    reg_date = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('court_cases_classification:upload_data')
    def __str__(self):
        return self.excel_file
        # return "%s - %s" % (self.level.class_name, self.level.class_name_in_numeric)


