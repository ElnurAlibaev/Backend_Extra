from rest_framework.viewsets import ViewSet
from . import models, serializers
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class CategoryView(ViewSet):

    def list(self, request, *args, **kwargs):
        categories=models.Category.objects.all()    

        serializer=serializers.CategorySerializer(categories, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        category=get_object_or_404(models.Category.objects.all(), pk=pk)

        serializer=serializers.CategorySerializer(category)

        return Response(serializer.data)

class ProductView(ViewSet):

    def list(self, request, *args, **kwargs):
        products=models.Product.objects.all()    

        serializer=serializers.ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        product=get_object_or_404(models.Product.objects.all(), pk=pk)

        serializer=serializers.ProductSerializer(product)

        return Response(serializer.data)

class CategoryProduct(ViewSet):

    def retrieve(self, request, pk):
        products=models.Product.objects.filter(category=pk)

        serializer=serializers.ProductSerializer(products, many=True)

        return Response(serializer.data)
