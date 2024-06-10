from django.contrib import admin
from .models import Blog,Author,userRegister,Img,category,product
# Register your models here.
class showBlog(admin.ModelAdmin):
    list_display=['name','tagline']
    list_filter=['name','tagline']
    search_fields=['name','tagline']

admin.site.register(Blog,showBlog)

class showAutor(admin.ModelAdmin):
    list_display=['name','email']
    list_filter=['name','email']
    search_fields=['name','email']

admin.site.register(Author,showAutor)


class showUser(admin.ModelAdmin):
    list_display=['name','email','add','password','mobile']
    list_filter=['name','email','add','password','mobile']
    search_fields=['name','email','add','password','mobile']

admin.site.register(userRegister,showUser)

class showImg(admin.ModelAdmin):
    list_display=['img']
    list_filter=['img']
    search_fields=['img']

admin.site.register(Img,showImg)

class showCategory(admin.ModelAdmin):
    list_display=['id','name','img']
    list_filter=['id','name','img']
    search_fields=['id','name','img']

admin.site.register(category,showCategory)

class showProduct(admin.ModelAdmin):
    list_display=['id','name','description','img','category','qty','price']
    list_filter=['id','name','description','img','category','qty','price']
    search_fields=['id','name','description','img','category','qty','price']

admin.site.register(product,showProduct)


