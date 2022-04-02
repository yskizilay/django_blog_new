from django.contrib import admin
from blog.models import KategoriModel
from blog.models.yazi import YazilarModeli

admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display=(
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )


admin.site.register(YazilarModeli,YazilarAdmin)

# Register your models here.
