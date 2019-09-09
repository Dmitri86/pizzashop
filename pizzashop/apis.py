from django.http import JsonResponse
from pizzashop.models import PizzaShop, Pizza

from pizzashop.serializers import PizzaShopSerializer, PizzaSerializer

def client_get_pizzashops(request):
    pizzashops = PizzaShopSerializer(
    PizzaShop.objects.all().order_by('-id'),
    many=True, context={'request': request}).data

    return JsonResponse({'pizzashops': pizzashops})


def client_get_pizzas(request, pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.all().filter(pizzashop_id=pizzashop_id).order_by('-id'), many=True,
        context={'request': request}
    ).data
    return JsonResponse({'pizzas': pizzas})