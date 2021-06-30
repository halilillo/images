import os

from django.db import models


class Image(models.Model):
    source = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-id']

    def filename(self):
        return os.path.basename(self.source.name)
    
    