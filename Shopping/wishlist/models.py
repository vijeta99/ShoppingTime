from django.db import models
from .scrapping import get_data 

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200)
    status=models.BooleanField(default=False)#discounted status
    cost=models.IntegerField(default=0)
    link=models.URLField()
    price_difference=models.FloatField(default=0)
    def __str__(self):
        return self.title
   
    def save(self, *args, **kwargs):
        name, price=get_data(self.link)
        if price:
            if price<self.cost:
                self.status=True
                self.price_difference=self.cost - price
                self.cost=price
                self.title=name

            
           # else:
               # self.cost=price
              #  self.title=name
        super().save(*args, **kwargs)
    
    