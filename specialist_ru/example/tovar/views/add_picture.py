from restful import restful
from ..forms import PictureForm
from django.db import connection
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

def picture(request, id):
    
    with connection.cursor() as cursor:
        cursor.execute(
            'select picture from tovar_tovar where id = %s ;',
            [id]
        )
        
        ( data, ) = cursor.fetchone()

        
    if not data:
        raise Http404()

    response = HttpResponse(content_type='image/jpeg', )
    response.write(data)

    return response



@restful
def add_picture(request, id):
    form = PictureForm()
    return render(request, 'tovar/add_picture.html', locals())


@add_picture.method('POST')
def add_picture(request, id):
    form = PictureForm(request.POST, request.FILES)

    if not form.is_valid():
        return render(request, 'tovar/add_picture.html', locals())

    data = b''

    for chunk in request.FILES['picture'].chunks():
        data += chunk

    with connection.cursor() as cursor:
        cursor.execute('update tovar_tovar set picture=%s where id=%s ;',
        [data, id]
        )

    return HttpResponseRedirect(reverse('tovar:price_list'))