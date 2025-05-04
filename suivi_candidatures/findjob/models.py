from django.db import models

class Application(models.Model):
    title = models.fields.CharField(max_length=100)
    link = models.fields.URLField(null=False,blank=False)
    applied = models.fields.BooleanField(default=False)
    date = models.fields.DateField()
