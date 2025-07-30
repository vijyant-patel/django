from django.db import models

class ZipFileUpload(models.Model):
    file = models.FileField(upload_to='zips/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
