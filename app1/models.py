from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.email

class userRegister(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    add=models.TextField()
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10,default='')
    
    def __str__(self):
        return self.name

class Img(models.Model):
    img=models.ImageField(upload_to='img/')
    

class category(models.Model):
    name=models.CharField(max_length=44)
    img=models.ImageField(upload_to='img') 
    def __str__(self):
     return self.name
    

class product(models.Model):
    name=models.CharField(max_length=44)
    description=models.TextField()
    img=models.ImageField() 
    price=models.CharField(max_length=5)
    qty=models.PositiveIntegerField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
     return self.name
    
class order(models.Model):
    userid = models.CharField(max_length=3)
    proid = models.CharField(max_length=3)
    add = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    qty = models.CharField(max_length=5)
    pincode = models.CharField(max_length=6)
    totalprice = models.CharField(max_length=6)
    orderid = models.CharField(max_length=50)
    paytype = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100) 
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userid


