from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.utils import timezone

from .models import Item, OrderItem, Order
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
    paginate_by = 10
    template_name = "store.html"


class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            return redirect("/")


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the item order is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
        else:
            # add a msg saying the order doesnt contain the item
            return redirect("core:product", slug=slug)
    else:
        # add a msg saying the user doesnt have an order
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)


def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            return redirect("core:order-summary")
        else:
            # add a msg saying the order doesnt contain the item
            return redirect("core:product", slug=slug)
    else:
        # add a msg saying the user doesnt have an order
        return redirect("core:product", slug=slug)
