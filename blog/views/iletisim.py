from django.shortcuts import render

def iletisim(request):
    context = {
        'sayi' : 6
    }

    return render(request, 'pages/iletisim.html', context=context)