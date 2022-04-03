from django.shortcuts import render
from blog.models import YazilarModel



def anasayfa(request):
    yazilar = YazilarModel.objects.all()
    return render(request, 'pages/anasayfa.html', context = {
        'yazilar': yazilar
    })