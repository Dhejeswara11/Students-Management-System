from rest_framework import serializers
from .models import Stocks, Category


class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
        class Meta:
            model = Stocks
            fields = "__all__"

        def to_representation(self, instance):
            self.fields['categoryId'] = CategorySerializer(read_only=True)
            return super(StockSerializer, self).to_representation(instance)


