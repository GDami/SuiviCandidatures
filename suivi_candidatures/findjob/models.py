from django.db import models

class Company(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    name = models.fields.CharField(max_length=30)

class Application(models.Model):
    title = models.fields.CharField(max_length=100)
    link = models.fields.URLField(null=False,blank=False)
    applied = models.fields.BooleanField(default=True)
    date_applied = models.fields.DateField(null=True, blank=True)
    called_back = models.fields.BooleanField(default=False)
    date_callback = models.fields.DateField(null=True, blank=True)
    cover_letter = models.fields.TextField(max_length=2000, default="", null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

