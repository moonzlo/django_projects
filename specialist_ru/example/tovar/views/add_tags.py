
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from ..models import Tovar, Tag
from ..forms import TagListForm
from restful import restful
from textwrap import dedent

@restful
def add_tags(request, id):
    tovar = get_object_or_404(Tovar, pk=id)
    form = TagListForm()

    return render(request, 'tovar/add_tags.html', locals())

@add_tags.method('POST')
def add_tags(request, id):
    
    form = TagListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['tag_list']

        with connection.cursor() as cursor:
            for pk_tag in map(str.lower, map(str.strip, tag_list.split(','))):
                
                cursor.execute(dedent('''\
                    insert into tovar_tag ( title )
                        values ( %s ) 
                        on conflict do nothing ;'''), 
                        [ pk_tag ]
                )
                cursor.execute(dedent('''\
                    insert into tovar_tovar_tags ( tovar_id, tag_id )
                        values ( %s, %s ) 
                        on conflict do nothing ;'''), 
                        [ id, pk_tag ]
                )

    tovar = get_object_or_404(Tovar, pk=id)
    return render(request, 'tovar/add_tags.html', locals())
