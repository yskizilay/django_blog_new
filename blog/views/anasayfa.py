from django.shortcuts import render



def anasayfa(request):
    context = {
        'isim' : 'Yunus KIZILAY____'
    }

    return render(request, 'pages/anasayfa.html', context = context)