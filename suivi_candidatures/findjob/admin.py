from django.contrib import admin

from findjob.models import Application, Company, Callback

admin.site.register(Application)
admin.site.register(Company)
admin.site.register(Callback)