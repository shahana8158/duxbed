from django.db import models

from django.contrib.auth.models import User



# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField (max_length=30,null=True,blank=True)
    details = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='products/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class fill_your_cart(models.Model):
    title = models.CharField(max_length=30)
    details = models.TextField()
    price = models.CharField (max_length=30)
    image=models.ImageField(upload_to='fill_your_cart')
   
   

    def __str__(self):
        return self.title
    

from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
    




class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"




from django.db import models

class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} from {self.location}"


# models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
