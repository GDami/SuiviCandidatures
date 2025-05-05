from django.shortcuts import render, redirect, get_object_or_404

from findjob.models import Application
from findjob.forms import ApplicationForm

def application_list(request):
    applications = Application.objects.all().order_by('date_applied')

    return render(request,
                  'findjob/application_list.html',
                  {'applications':applications}
                  )

def application_detail(request, id):
    application = get_object_or_404(Application, id=id)

    return render(request,
                  'findjob/application_detail.html',
                  {'application':application}
                  )

def application_add(request):
    if request.method == 'GET':
        form = ApplicationForm()
    
    elif request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()

            return redirect('application-detail', application.id)

    return render(request,
                  'findjob/application_add.html',
                  {'form':form}
                  )