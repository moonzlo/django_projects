from django.shortcuts import render
from ..models import Group


def group_list(request):
    groups = Group.objects.all()
    context = {

        'groups': groups
    }

    return render(request, 'tovar/groups.html', context)
