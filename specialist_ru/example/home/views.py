from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

def home_page(request):
    local_time = datetime.now()

    context = {

        'local_time': local_time
    }

    return render(request, 'main.html', context)