from django.urls import path

from visits.views import Visiting

urlpatterns = [
    path('', Visiting.as_view(), name='visits')
]
