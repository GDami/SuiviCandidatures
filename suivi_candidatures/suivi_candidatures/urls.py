"""
URL configuration for suivi_candidatures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from findjob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applications/', views.application_list, name='application-list'),
    path('applications/<int:id>/', views.application_detail, name='application-detail'),
    path('applications/<int:id>/delete', views.application_delete, name='application-delete'),
    path('applications/<int:id>/accepted', views.application_accepted, name='application-accepted'),
    path('applications/<int:id>/declined', views.application_declined, name='application-declined'),
    path('applications/add/', views.application_add, name='application-add'),
    path('applications/export-csv/', views.application_export_csv, name='application-export-csv'),
    path('companies/', views.company_list, name='company-list'),
    path('companies/<int:id>/', views.company_detail, name='company-detail'),
    path('companies/<int:id>/delete', views.company_delete, name='company-delete'),
    path('companies/add/', views.company_add, name='company-add'),
    path('applications/<int:id>/callback/add', views.callback_add, name='callback-add'),
]
