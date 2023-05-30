from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    title = models.CharField(max_length=200, blank=True, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='/walker.jpg')
    brand = models.CharField(max_length=200, null=True, blank=True)
    # category = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)    
    price = models.IntegerField( null=True, blank=True)    
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    
    def __str__(self) -> str:
        return self.name





class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return str(self.rating)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    # taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)    
    taxPrice = models.IntegerField(null=True, blank=True)    
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)    
    # totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)    
    totalPrice = models.IntegerField(null=True, blank=True)    
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt =  models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.createdAt)




class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)    
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)


    def __str__(self) -> str:
        return str(self.name)




class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)    
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.address)
