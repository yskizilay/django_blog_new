from unittest.util import _MAX_LENGTH
from django import forms


class IletisimForm(forms.Form):
    email = forms.EmailField(label='E-Posta', max_length=100)
    isim_soyisim = forms.CharField(label= 'Ad Soyad', max_length=25)
    mesaj = forms.CharField(label= 'Mesajınız', widget=forms.Textarea)