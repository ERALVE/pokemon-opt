from django.shortcuts import render

# Create your views here.

def owner_list(request):

    data_context= {
        'nombre':  'Samanta Peralta',
        'edad': 20,
        'dni': "1234567",
        'pais': "Perú",
        'vigente': False,
    }

    return render(request, 'owner_list.html', context={'data': data_context})
