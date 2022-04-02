from django.contrib import admin
from blog.models import (
KategoriModel, YazilarModel, YorumModel
)


admin.site.register(KategoriModel)

class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display=(
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )


admin.site.register(YazilarModel,YazilarAdmin)

class YorumAdmin(admin.ModelAdmin):
    search_fields = ('yazan__username',)
    list_display = ('yazan', 'olusturulma_tarihi', 'guncellenme_tarihi')
    


admin.site.register(YorumModel, YorumAdmin)
