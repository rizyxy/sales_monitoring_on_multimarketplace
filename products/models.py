from django.db import models

class OnlineShop(models.Model):
    olshop_name = models.CharField(max_length=255)
    olshop_city = models.CharField(max_length=255)

class Product(models.Model):
    product_url = models.TextField()
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    online_shop = models.ForeignKey(OnlineShop, on_delete=models.CASCADE)

class ProductHistory(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    review_count = models.IntegerField()
    rating = models.FloatField()
    sold_count = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
