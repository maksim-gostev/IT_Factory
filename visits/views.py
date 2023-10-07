import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_400_BAD_REQUEST
from a_store.models import A_Stores
from visits.models import Visits
from visits.serializers import VisitingSerializer


@method_decorator(csrf_exempt, name='dispatch')
class Visiting(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        phone = request.GET.get('phone', None)
        if phone is None:
            return JsonResponse({'message': 'Вы не ввели телефон работника'},
                                safe=False, status=HTTP_400_BAD_REQUEST)

        a_store = A_Stores.objects.filter(id=data['id']).all()
        if a_store[0].worker.phone_number == phone:
            visiting = Visits()
            visiting.a_store = a_store[0]
            visiting.latitude = data['latitude']
            visiting.longitude = data['longitude']
            visiting.save()
            return JsonResponse(VisitingSerializer(visiting).data, safe=False)
        return JsonResponse({'message': 'Не верный номер телефона'},
                            safe=False, status=HTTP_400_BAD_REQUEST)