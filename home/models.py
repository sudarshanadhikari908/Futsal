from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email =models.CharField(max_length=30)
    phone = models.CharField(max_length = 12)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.CharField(max_length=300)
    pubdate = models.DateTimeField()
    image = models.ImageField(upload_to="home/img", default="")

    def __str__(self):
        return self.product_name

 
    