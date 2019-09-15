from django.shortcuts import render
from ..models import Tag


def tag_list(request):
    tags = Tag.objects.all()

    context = {

        'tags': tags
    }

    return render(request, 'tovar/tags.html', context)
