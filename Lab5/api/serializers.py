from rest_framework import serializers
from api import models

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'

class _ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
        )

class ProductSerializer(serializers.ModelSerializer):
    category = _ProductCategorySerializer(read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'