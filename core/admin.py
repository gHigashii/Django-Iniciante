from django.contrib import admin

from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'formatted_price', 'stock')

    def formatted_price(self, obj):
        return f'RS: {obj.price}'.replace('.', ',')
    formatted_price.short_description = 'price'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)