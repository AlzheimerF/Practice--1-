from .models import Shop, Goods
from rest_framework import serializers


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.save()
            return instance


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'title', 'description', 'quantity', 'branch']

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.branch = validated_data.get('branch', instance.branch)
            instance.save()
            return instance