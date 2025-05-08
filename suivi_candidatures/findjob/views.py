from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta

from findjob.models import Application, Company
from findjob.forms import AddApplicationForm, CompanyForm, AddCallbackForm



def application_list(request):
    if request.GET:
        match (request.GET["filter"]):
            case 'open':
                display = 'Candidatures en cours'
                applications = Application.objects.all().filter(state__exact='OP').order_by('date_applied')
            case 'accepted':
                display = 'Candidatures acceptées'
                applications = Application.objects.all().filter(state__exact='OK').order_by('date_applied')
            case 'declined':
                display = 'Candidatures refusées'
                applications = Application.objects.all().filter(state__exact='NO').order_by('date_applied')
            case 'called_back':
                display = 'Candidatures relancées'
                applications = Application.objects.all().filter(called_back__exact=True).order_by('date_applied')
            case 'need_callback':
                display = 'Candidatures à rappeler'
                all_applications = Application.objects.all().exclude(state__exact='NO').order_by('date_applied')
                applications = []
                now = datetime.now().date()

                for application in all_applications:
                    should_callback = now - application.date_applied >= timedelta(7)
                    if application.state == Application.ApplicationState.OPEN and not application.called_back and should_callback:
                        applications.append(application)
    else:
        display = 'Toutes les candidatures'
        applications = Application.objects.all().order_by('date_applied')
    
    return render(request,
                  'findjob/application_list.html',
                  {'applications':applications, 'display':display}
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