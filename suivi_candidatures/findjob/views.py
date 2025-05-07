from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta

from findjob.models import Application, Company
from findjob.forms import AddApplicationForm, CompanyForm, AddCallbackForm

def application_list(request):
    applications = Application.objects.all().order_by('date_applied')
    need_callback = []
    now = datetime.now().date()

    for application in applications:
        should_callback = now - application.date_applied >= timedelta(7)
        if application.state == Application.ApplicationState.OPEN and not application.called_back and should_callback:
            need_callback.append(application)

    return render(request,
                  'findjob/application_list.html',
                  {'applications':applications, 'need_callback':need_callback}
                  )

def application_detail(request, id):
    application = get_object_or_404(Application, id=id)

    return render(request,
                  'findjob/application_detail.html',
                  {'application':application}
                  )

def application_add(request):
    if request.method == 'GET':
        form = AddApplicationForm()
    
    elif request.method == 'POST':
        form = AddApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()

            return redirect('application-detail', application.id)

    return render(request,
                  'findjob/application_add.html',
                  {'form':form}
                  )

def application_delete(request, id):
    application = get_object_or_404(Application, id=id)

    return render(request,
                  'findjob/application_delete',
                  {'application':application}
                  )

def application_accepted(request, id):
    application = get_object_or_404(Application, id=id)
    application.state = Application.ApplicationState.ACCEPTED
    application.save()

    return redirect('application-detail', application.id)

def application_declined(request, id):
    application = get_object_or_404(Application, id=id)
    application.state = Application.ApplicationState.DECLINED
    application.save()

    return redirect('application-detail', application.id)

def company_list(request):
    companies = Company.objects.all().order_by('name')

    return render(request,
                  'findjob/company_list.html',
                  {'companies':companies}
                  )

def company_detail(request, id):
    company = get_object_or_404(Company, id=id)

    return render(request,
                  'findjob/company_detail.html',
                  {'company':company}
                  )

def company_add(request):
    if request.method == 'GET':
        form = CompanyForm()
    
    elif request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()

            return redirect('company-detail', company.id)

    return render(request,
                  'findjob/company_add.html',
                  {'form':form}
                  )

def callback_add(request, id):
    application = get_object_or_404(Application, id=id)

    if request.method == 'GET':
        form = AddCallbackForm()
    
    elif request.method == 'POST':
        form = AddCallbackForm(request.POST)
        if form.is_valid():
            callback = form.save()
            application.called_back = True
            application.callback = callback

            application.save()

            print(application)
            print(application.callback)

            return redirect('application-detail', application.id)
    
    return render(request,
                  'findjob/callback_add.html',
                  {'form':form}
                  )