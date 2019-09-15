from django.shortcuts import render
from ..models import Tovar



def show(request, id):
    tovar = Tovar.objects.get(pk=id)
    tags = ', '.join((tag.title for tag in tovar.tags.all()))
    context = {

        'tovar': tovar,
        'tags': tags
    }    
    return render(request, 'tovar/show.html', context)
