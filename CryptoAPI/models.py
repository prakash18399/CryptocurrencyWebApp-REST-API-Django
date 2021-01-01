from django.db import models

# Create your models here.
class Cryptocurrency(models.Model): 
    cryptocurrency = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100) 

    def __str__(self):
        return self.cryptocurrency

    

