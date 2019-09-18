from django.http import HttpResponse
import numpy as np
import matplotlib.pyplot as plt


def graph(request):
    x = np.linspace(-20, 20.0, 10000)
    y = np.sin(x) / x

    fig = plt.figure()
    axis = plt.subplot(111)
    axis.plot(x,y)

    response = HttpResponse(content_type='image/png')
    plt.savefig(response, format='jpg')

    return response