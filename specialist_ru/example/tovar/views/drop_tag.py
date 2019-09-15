from textwrap import dedent
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Tovar, Tag



def drop_tag(request, id, pk_tag):
    with connection.cursor() as cursor:
        cursor.execute(
            dedent('''\
                delete 
                   from tovar_tovar_tags 
                   where tovar_id = %s
                         and tag_id = %s ;'''),
            [id, pk_tag]
        )
    return HttpResponseRedirect(reverse('tovar:add_tags', args=[id]))