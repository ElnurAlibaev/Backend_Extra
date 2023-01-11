from django.db import models

class Category(models.Model):

    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):

    name=models.CharField(max_length=100)
    price=models.FloatField(default=1000.00)
    description=models.TextField(default='')
    quantity=models.IntegerField(default=1)
    is_active=models.BooleanField(default=False)

    category = models.ForeignKey( 
        to=Category,
        on_delete=models.CASCADE,  
        related_name='category',  
    )

    def __str__(self) -> str:
        return f'{self.name}'


