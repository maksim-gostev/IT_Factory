from django.http import JsonResponse
from django.views import View

from a_store.models import A_Stores
from a_store.serializers import A_StoreListSerializer


class GetA_StoreList(View):

    def get(self, request):
        a_stores = A_Stores.objects.all()
        phone = request.GET.get('phone', None)
        if phone:
            a_stores = A_Stores.objects.filter(worker__phone_number=phone).all()

        return JsonResponse(A_StoreListSerializer(a_stores, many=True).data, safe=False)
