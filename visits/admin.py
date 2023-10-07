from django.contrib import admin

from visits.models import Visits

class VisitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'a_store', 'data', 'latitude', 'longitude')
    search_fields = ('a_store__name', 'a_store__worker__name')


admin.site.register(Visits, VisitsAdmin)
