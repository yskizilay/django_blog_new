from django.shortcuts import get_object_or_404, redirect, render
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages
import logging

logger = logging.getLogger('konu_okuma')


class DetayView(View):
    http_method_name = ['get', 'post']
    yorum_ekle_form = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)

        logger.info('konu okundu:' + request.user.username)

        yorumlar = yazi.yorumlar.all()
        return render(request, 'pages/detay.html', context={
            'yazi': yazi, 
            'yorumlar': yorumlar,
            'yorum_ekle_form': self.yorum_ekle_form(),
        })
    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekle_form = self.yorum_ekle_form(request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, 'Yorum Başarılı bir şekilde eklendi.')
        return redirect('detay', slug=slug)


def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    yorumlar = yazi.yorumlar.all()
    if request.method == 'POST':
        yorum_ekle_form = YorumEkleModelForm(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()

    yorum_ekle_form = YorumEkleModelForm()



    return render(request, 'pages/detay.html', context={
        'yazi': yazi, 
        'yorumlar': yorumlar,
        'yorum_ekle_form': yorum_ekle_form
    })