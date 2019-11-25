from django.db import models

# Create your models here.


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    name = models.CharField(max_length=500)
    imagefile = models.FileField(upload_to='documents/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)
