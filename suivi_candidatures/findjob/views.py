from django.shortcuts import render

from findjob.models import Application

def application_list(request):
    application = Application.objects.all()

    return render(request,
                  'findjob/application_list.html',
                  {'application':application}
                  )

