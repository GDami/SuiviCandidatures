from django.shortcuts import render, redirect, get_object_or_404

from findjob.models import Application, Company
from findjob.forms import AddApplicationForm, CompanyForm, AddCallbackForm

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