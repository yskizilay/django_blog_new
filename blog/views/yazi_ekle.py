from django import template
from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from blog.models import YazilarModel
from django.urls import reverse

class YaziEkleCreateView(CreateView):
    template_name = ('pages/yazi-ekle.html')
    model = YazilarModel
    fields = ('baslik', 'icerik', 'resim', 'kategoriler')

    def get_success_url(self) -> str:
        return reverse('detay', kwargs={
            'slug': self.object.slug
        })


    def form_valid(self, form):
        yazi = form.save(commit=False)
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m()
        return super().form_valid(form)    


@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug=yazi.slug)

    return render(request, 'pages/yazi-ekle.html', context={
        'form' : form
    })