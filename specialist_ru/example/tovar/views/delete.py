from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Tovar


def delete(request, id):
    tovar = get_object_or_404(Tovar, pk=id)
    tovar.delete()
    return HttpResponseRedirect(reverse('tovar:price_list'))