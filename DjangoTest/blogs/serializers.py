from rest_framework import serializers
from . import models

class BlogSerializer(serializers.Serializer):     #Это общий сериалайзер
    id=serializers.IntegerField(read_only=True)   #read_only чтобы его не передавать, создавался автоматически
    title=serializers.CharField(max_length=100)
    blog=serializers.CharField()

class BlogModelSerializer(serializers.ModelSerializer):    #Сериалайзер привязанный к конкертной модельке

    class Meta:
        model=models.Blog
        fields="__all__"
        #fields=('id', 'title')  Можно выбрать столбцы