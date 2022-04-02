from django.contrib import admin
from blog.models import (
KategoriModel, YazilarModel, YorumModel, IletisimModel
)


admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display=(
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    search_fields = ('yazan__username',)
    list_display = ('yazan', 'olusturulma_tarihi', 'duzenlenme_tarihi')
    


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = ('email', 'olusturulma_tarihi')


