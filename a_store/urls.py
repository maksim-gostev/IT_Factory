from django.urls import path

from a_store.views import GetA_StoreList

urlpatterns = [
    path('', GetA_StoreList.as_view(), name='a_store')
]
