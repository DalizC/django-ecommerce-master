from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView

from .models import Item
from .serializers import ItemSerializer


@csrf_exempt
def itemApi(request, id=0):
    if request.method == 'GET':
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class StoreView(ListView):
    model = Item
    template_name = "store.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

# def item_list(request):
#    context = {
#        'items': Item.objects.all()
#    }
#    return render(request, "home.html", context)
