from django.shortcuts import render, redirect

from .forms import LegalEntityForm
from .model import LegalEntity
from .serialize import LegalEntitySerializer


def LegalEntityGetAll(request):
    all_legal_entity = LegalEntity.objects.all ()
    return render ( request, "legal_entity_list.html", {'legal_entity': all_legal_entity} )


def LegalEntityDelete(request, pk):
    legal_entity_obj = LegalEntity.objects.filter ( pk=pk )
    if not legal_entity_obj.exists ():
        return render ( request, "legal_entity_is_delete.html", {'delete_le': None} )
    les = LegalEntitySerializer ()
    les.delete ( legal_entity_obj )
    return render ( request, "legal_entity_is_delete.html", {'delete_le': legal_entity_obj} )


def LegalEntityUpdate(request, pk):
    legal_entity_obj = LegalEntity.objects.filter ( pk=pk )
    if not legal_entity_obj.exists ():
        return render ( request, "legal_entity_is_update.html", {'update_le': None} )
    if request.method == "POST":
        form = LegalEntityForm ( request.POST, instance=legal_entity_obj.first () )
        if form.errors:
            return render ( request, 'legal_entity_is_update.html', {'update_le': None} )
        legal_entity = form.save ( commit=False )
        legal_entity.id_client = request.POST['id_client']
        legal_entity.name_short = request.POST['name_short']
        legal_entity.name_full = request.POST['name_full']
        legal_entity.inn = request.POST['inn']
        legal_entity.kpp = request.POST['kpp']
        legal_entity.save ()
        return render ( request, 'legal_entity_is_update.html', {'update_le': legal_entity} )
    else:
        form = LegalEntityForm ( instance=legal_entity_obj.first () )
    return render ( request, 'create.html', {'form': form} )


def LegalEntityCreate(request):
    if request.method == 'POST':
        form = LegalEntityForm ( request.POST )
        if form.errors:
            return render ( request, 'legal_entity_is_success.html', {'add_le': None} )
        form.save()

        legal_entity_obj = LegalEntity.objects.filter ( id_client=request.POST['id_client'] ).first ()
        return render ( request, 'legal_entity_is_success.html', {'add_le': legal_entity_obj} )
    else:
        form = LegalEntityForm ()
        return render ( request, "create.html", {'form': form} )

