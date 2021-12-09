from django.shortcuts import render, redirect

from .forms import ClientForm
from .model import Client
from .serialize import ClientSerializer


def ClientGetAll(request):
    all_client = Client.objects.all ()
    return render ( request, "client_list.html", {'legal_entity': all_client} )


def ClientDelete(request, pk):
    client_obj = Client.objects.filter ( pk=pk )
    if not client_obj.exists ():
        return render ( request, "client_is_delete.html", {'delete_client': None} )
    client = ClientSerializer ()
    client.delete ( client_obj)
    return render ( request, "client_is_delete.html", {'delete_client': client_obj} )


def ClientUpdate(request, pk):
    client_obj = Client.objects.filter ( pk=pk )
    if not client_obj.exists ():
        return render ( request, "client_is_update.html", {'update_client': None} )
    if request.method == "POST":
        form = ClientForm ( request.POST, instance=client_obj.first () )
        if form.errors:
            return render ( request, 'client_is_update.html', {'update_le': None} )
        client = form.save ( commit=False )
        client.id_client = request.POST['id_client']
        client.phone_number = request.POST['phone_number']
        client.additional_numbers = request.POST['additional_numbers']
        client.surname = request.POST['surname']
        client.name = request.POST['name']
        client.middle_name = request.POST['middle_name']
        client.status = request.POST['status']
        client.type_of_client = request.POST['type_of_client']
        client.email = request.POST['email']
        client.timezone = request.POST['timezone']
        client.sex = request.POST['sex']
        client.save ()
        return render ( request, 'client_is_update.html', {'update_client': client} )
    else:
        form = ClientForm ( instance=client_obj.first() )
    return render ( request, 'create.html', {'form': form} )


def ClientCreate(request):
    if request.method == 'POST':
        form = ClientForm ( request.POST )
        if form.errors:
            return render ( request, 'client_is_success.html', {'add_client': None} )
        form.save(commit=True)
        client_obj = Client.objects.filter ( id_client=request.POST['id_client'] ).first ()
        return render ( request, 'client_is_success.html', {'add_client': client_obj} )
    else:
        form = ClientForm()
        return render ( request, "create.html", {'form': form} )
