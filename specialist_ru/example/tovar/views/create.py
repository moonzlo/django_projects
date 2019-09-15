from ..forms import ToavrModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Tovar
from restful import restful


@restful
def create(request):
    tovar = Tovar()
    form = ToavrModelForm(instance=tovar)

    return render(request, 'tovar/edit.html', locals())


@create.method('POST')
def create(request):
    tovar = Tovar()
    form = ToavrModelForm(request.POST, instance=tovar)

    if form.is_valid():
        tovar = form.save()
        return HttpResponseRedirect(reverse('tovar:show', args=[tovar.pk]))

    else:
        return render(request, 'tovar/edit.html', locals())