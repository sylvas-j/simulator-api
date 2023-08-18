from django.db import models
from django.conf import settings
from django.urls import reverse



class UploadData(models.Model):

    pred_range = models.CharField(max_length=10)
    excel_file = models.FileField(upload_to='data_files')
    reg_date = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('smart_home_monitoring:upload_data')
    def __str__(self):
        return self.excel_file
        # return "%s - %s" % (self.level.class_name, self.level.class_name_in_numeric)


