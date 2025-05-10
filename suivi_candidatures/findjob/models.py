from django.db import models

class Company(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    name = models.fields.CharField(max_length=30, unique=True)

class Callback(models.Model):
    date = models.fields.DateField()
    message = models.fields.TextField(max_length=2000)

class Application(models.Model):
    class ApplicationState(models.TextChoices):
        OPEN = 'OP'
        DECLINED = 'NO'
        ACCEPTED = 'OK'

    title = models.fields.CharField(max_length=100)
    link = models.fields.URLField(null=False,blank=False)
    applied = models.fields.BooleanField(default=True)
    date_applied = models.fields.DateField(null=True, blank=True)
    cover_letter = models.fields.TextField(max_length=2000, default="", null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    state = models.fields.CharField(choices=ApplicationState.choices, max_length=2, default=ApplicationState.OPEN)
    called_back = models.fields.BooleanField(default=False)
    callback = models.OneToOneField(Callback, null=True, blank=True, on_delete=models.SET_NULL)