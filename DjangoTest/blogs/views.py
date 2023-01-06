from . import models, serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet


def index(request):
    blogs=models.Blog.objects.all()   #ORM
    blog_titles=[{'title':b.title} for b in blogs]
    blog=blogs.get(id=1)

    #return JsonResponse(blog_titles, safe=False)

    return JsonResponse({
        'id':blog.id,
        'title':blog.title,
        'body':blog.body,
    })

@api_view(['GET'])
def get_blogs(request, *args, **kwargs):   #args, kwargs можно не писать
    blog=models.Blog.objects.all()    
    #blog=models.Blog.objects.filter(id__gt=1)  Блоги в которых id greater than 1, можно gte включая

    serializer=serializers.BlogModelSerializer(blog, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_blog(request, *args, **kwargs):
    blog=get_object_or_404(models.Blog.objects.all(), **kwargs)   # object с определённой id из url

    serializer=serializers.BlogModelSerializer(blog)

    return Response(serializer.data)

@api_view(['POST'])
def create_blog(request):

    serializer=serializers.BlogModelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)  # Проверяет данные, если неправильно выдаёт ошибку

    blog=models.Blog.objects.create(**serializer.validated_data)   # Создаём новый блог

    return Response(serializers.BlogModelSerializer(blog).data, status=status.HTTP_201_CREATED)  # Можно поменять статус

class BlogView(APIView):

    def get(self, request, *args, **kwargs):
        blog=models.Blog.objects.all()    

        serializer=serializers.BlogModelSerializer(blog, many=True)

        return Response(serializer.data)

class BlogView2(ViewSet):

    def list(self, request, *args, **kwargs):
        blog=models.Blog.objects.all()    

        serializer=serializers.BlogModelSerializer(blog, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        blog=get_object_or_404(models.Blog.objects.all(), pk=pk)

        serializer=serializers.BlogModelSerializer(blog)

        return Response(serializer.data)

class BlogListCreateAPIView(CreateAPIView, ListAPIView):

    queryset=models.Blog.objects.all()
    serializer_class=serializers.BlogModelSerializer

class BlogViewSet(ModelViewSet):

    queryset=models.Blog.objects.all()
    serializer_class=serializers.BlogModelSerializer