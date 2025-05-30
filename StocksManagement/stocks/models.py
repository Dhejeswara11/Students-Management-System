
from django.db import models



class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=25)


class Stocks(models.Model):
   
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity =models.IntegerField()
    createdDateTime = models.DateTimeField(auto_now_add=True)
    categoryId = models.ForeignKey(Category,
                                   on_delete=models.CASCADE,
                                   related_name='stocks')


