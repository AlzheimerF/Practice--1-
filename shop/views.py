from django.shortcuts import render
from .models import Shop, Goods
from rest_framework.decorators import api_view
from rest_framework.views import Response
from .serializers import ShopSerializers, GoodsSerializers


@api_view(["GET"])
def all_shops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializers(shops, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def about_shop(request, id):
    shop = Shop.objects.get(id=id)
    goods = Goods.objects.filter(branch=id)
    serializer = ShopSerializers(shop)
    serializer1 = GoodsSerializers(goods, many=True)
    return Response([serializer.data, serializer1.data])

@api_view(['POST'])
def add_goods(request):
     serializer = GoodsSerializers(data=request.data)
     if serializer.is_valid():
         serializer.save()
     return Response({'Товар': 'Успешно создан!'})

@api_view(['POST'])
def add_shop(request):
    serializer = ShopSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Магазин': 'Успешно создан!'})

@api_view(['DELETE'])
def delete_goods(request, id):
    delete_goods = Goods.objects.get(id=id)
    if delete_goods:
        delete_goods.delete()
        return Response({'Товар': 'Успешно удален!'})

@api_view(['DELETE'])
def delete_shop(request, id):
    delete_shop = Shop.objects.get(id=id)
    if delete_shop:
        delete_shop.delete()
        return Response({'Магазин': 'Успешно удален!'})

@api_view(['POST'])
def update_shop(request, id):
    shop = Shop.objects.get(id=id)
    serializer = ShopSerializers(instance=shop, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_goods(request, id):
    goods = Goods.objects.get(id=id)
    serializer = GoodsSerializers(instance=goods, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


