from django.shortcuts import render
from ..models import Tovar, Tag


def price_list(request):
    item_list = Tovar.objects.all()

    return render(request, 'tovar/index.html', locals())
