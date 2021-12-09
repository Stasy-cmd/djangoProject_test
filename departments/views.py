from django.shortcuts import render

from departments.forms import DepartmentsForm, LegalClientForm, DepartmentsLegalForm
from departments.model import Departments


def DepartmentGetAll(request):
    departments = Departments.objects.all ()
    return render ( request, "departments_list.html", {'departments': departments} )


def DepartmentsCreate(request):
    if request.method == 'POST':
        form = DepartmentsForm ( request.POST )
        if form.errors:
            return render ( request, 'success.html', {'add': False} )
        form.save ()
        return render ( request, 'success.html', {'add': True} )
    else:
        form = DepartmentsForm ()
        return render ( request, "create.html", {'form': form} )



def DepartmentLegalCreate(request):
    if request.method == 'POST':
        form = DepartmentsLegalForm ( request.POST )
        if form.errors:
            return render ( request, 'success.html', {'add': False} )
        form.save ()
        return render ( request, 'success.html', {'add': True} )
    else:
        form = DepartmentsLegalForm ()
        return render ( request, "create.html", {'form': form} )


def LegalClientCreate(request):
    if request.method == 'POST':
        form = LegalClientForm ( request.POST )
        if form.errors:
            return render ( request, 'success.html', {'add': False} )
        form.save ()
        return render ( request, 'success.html', {'add': True} )
    else:
        form = LegalClientForm()
        return render ( request, "create.html", {'form': form} )


