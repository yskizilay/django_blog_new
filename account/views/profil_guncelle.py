from django.shortcuts import  redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm

@login_required(login_url='/')
def profil_guncelle(request):

    if request.method == 'POST':
        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil Başarılı bir şekilde güncellendi')
    else:
        form = ProfilDuzenlemeForm(instance = request.user)

    return render(request, 'pages/profil-guncelle.html', context={
        'form' : form
    })