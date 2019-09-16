from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from restful import restful
from ..models import Tovar, Group, Tag
from ..forms import TovarForm, ToavrModelForm
import sys

@restful
def edit(request, id):

    tovar = Tovar.objects.get(pk=id)
    form = ToavrModelForm(instance=tovar)

    return render(request, 'tovar/edit.html', locals())   


@edit.method('POST')
def edit(request, id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tovar:show', args=[id]))

    if not request.user.is_superuser:
        if not request.user.has_perm('tovar.change_tovar'):
            return HttpResponseRedirect(reverse('tovar:show', args=[id]))



    raw_data = dict()
    raw_data.update(request.POST)

    tovar = Tovar.objects.get(pk=id)
    form = ToavrModelForm(request.POST, instance=tovar)
    if form.is_valid():
        form.save()
        return render(request, 'tovar/show.html', locals())
        
    else:
        return render(request, 'tovar/edit.html', locals())  
  
