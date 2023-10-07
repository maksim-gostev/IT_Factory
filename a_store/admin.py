from django.contrib import admin

from a_store.models import Workers, A_Stores

class WorkersAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('name', 'phone_number')
    search_fields = ('name',)
    fields = ('name', 'phone_number')
    save_on_top = True


class A_StoresAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'worker')
    list_display_links = ('name', 'worker')
    search_fields = ('name',)
    save_on_top = True


admin.site.register(A_Stores, A_StoresAdmin)
admin.site.register(Workers, WorkersAdmin)
