from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField


# 1 способ создания объекта базы данных 
blog=Blog(title="title 1", body="body 1")
blog.save()

# 2 способ создания объекта базы данных 
blog=Blog.objects.create(title="title 1", body="body 2")
