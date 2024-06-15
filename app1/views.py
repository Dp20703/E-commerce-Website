from django.shortcuts import render,HttpResponse,redirect
from  .models import *

# Create your views here.
def Default(request):
    return render(request,'first.html')
def first(request):
    return HttpResponse("This is my first function")


# send the data by form function to the Author database using form.html: 
def form(request):
   if request.method=='POST':
        # print(1111)
        storeauthor=Author()
        storeauthor.name=request.POST['uname']
        storeauthor.email=request.POST['email']
        storeauthor.save()
        # print(2222)
        return render(request,'form.html')
   else:
      return render(request,'form.html')
   
# for showing data of Author database by table function using table.htnl: 
def table(request):
    authordata =Author.objects.all()
    # print(authordata)
    # for i in authordata:
        # print(i)
        # print(i.name)
        # print(i.email)
    return render(request,'table.html',{'author':authordata})

# send the data from category form to the database using Cform.html: 
def Cform(request):
   if request.method=='POST':
        storeCategory=category()
        storeCategory.name=request.POST['uname']
        storeCategory.img=request.FILES['img']
        storeCategory.save()
        return render(request,'Cform.html')
   else:
      return render(request,'Cform.html')
   
# for showing data of Category in the categoryTable using category.htnl:
def CategoryTable(request):
    categorydata =category.objects.all()   
    return render(request,'category.html',{'category':categorydata})
     

#For showing the data of Author and updating the values by updata function using update.html
def update(request):
    try:
        authordata=Author.objects.get(name='dp')
        if request.method=="POST":
            print(1111)
            # authordata=Author.objects.get(name='darshan')
       #For updating the author data:
            authordata.name=request.POST['uname']
            authordata.email=request.POST['email']
            authordata.save()
            print(333333)
       #For showing the author data:
            print(authordata)
            return render(request,'update.html',{'author':authordata})
        else:
        #  authordata=Author.objects.get(name='darshan')
         return render(request,'update.html',{'author':authordata})
    except Exception as e:
        return render(request,'update.html')


  #For Showing the form data from database to the update form in the web browser:
# def update2(request):
#         authordata=Author.objects.get(name='Darshan')
#         print(authordata)
#         return render(request,'update2.html',{'author':authordata})


def index(request):
 if 'email' in request.session:
    categorydata=category.objects.all()
    return render(request,'index.html',{'catdata':categorydata,'session':True})
 else:
      categorydata=category.objects.all()
      return render(request,'index.html',{'catdata':categorydata})


def allproduct(request):
    productdata=product.objects.all()
    return render(request,"product.html",{'proData':productdata})


def register(request):
    if request.method=="POST":
        user =userRegister()
        user.name=request.POST['name']
        user.email=request.POST['email']
        user.add=request.POST['add']
        user.mobile=request.POST['mobile']
        user.password=request.POST['password']
        userAlready=userRegister.objects.filter(email=request.POST['email'])
        if len(userAlready) > 0:
                    return render(request,"register.html",{'userAlready':'This email is already registered'})
        else:
              if request.POST['cpassword']!=request.POST['password']:
               return render(request,'register.html',{"passnotmatch":'Confirm password is not mathced!'})
              else:
                user.save()
                return render(request,"register.html",{'store':'You are registered Successfully'})
    else:
        return render(request,"register.html")
   
def Login(request):
 if request.method=="POST":
    try:
        user=userRegister.objects.get(email=request.POST['email'])
        if user.password == request.POST['password']:
          request.session['email']=user.email
        #   print(request.session['email'])
          return redirect("index")     
        else:
            return render(request,"login.html",{'pass':'Password is incorrect...'})
    except Exception as e:
     return render(request,"login.html",{'notregistered':'Before login you have to register first!'})  
 else:
         return render(request,"Login.html")
      

def logout(request):
    del request.session['email']
    return redirect('index')


def catproduct(request,id):
 if 'email' in request.session:
    catpro=product.objects.filter(category = id)
    return render(request,'catProduct.html',{'catpro':catpro,'session':True})
 else:
     catpro=product.objects.filter(category = id)
     return render(request,'catProduct.html',{'catpro':catpro})

def proDetails(request,id):
   if 'email' in request.session:
        pro=product.objects.get(pk = id)
        if request.method == 'POST':
            print(1111111)
            qty = request.POST['qty']
            print(qty)
            request.session['qty'] = qty
            request.session['proid'] = id
            # return render(request,'proDetails.html',{'pro':pro,'session':True})
            return redirect("checkout")
            # return render(request,'checkout.html',{'pro':pro,'session':True})
        else:
             return render(request,'proDetails.html',{'pro':pro,'session':True})
   else:
        pro=product.objects.get(pk = id)
        return  render(request,'proDetails.html',{'pro':pro})
    

def profile(request):
    if 'email' in request.session:
        userdetails=userRegister.objects.get(email=request.session['email'])
        if request.method=='POST':
            userdetails.name=request.POST['name']
            userdetails.mobile=request.POST['mobile']
            userdetails.add=request.POST['add']
            userdetails.save()
            return render(request,'profile.html',{'user':userdetails,'session':True})
        else:
            return render(request,'profile.html',{'user':userdetails,'session':True})
    else:
     return redirect('Login')
    
import random
def checkout(request):
    if 'email' in request.session:
        print(111111)
        user=userRegister.objects.get(email=request.session['email'])
        pro=product.objects.get(id=int(request.session['proid']))
        orderid=random.randint(0000000,9999999)
        print(2222222)
        if request.method=='POST':
            print(3333333333)

            orderdata=order()
            orderdata.userid=user.pk
            orderdata.proid=request.session["proid"]
            orderdata.add=request.POST['add']
            orderdata.city=request.POST['city']
            orderdata.state=request.POST['state']
            orderdata.pincode=request.POST['pin']
            orderdata.qty=request.session['qty']
            orderdata.orderid=orderid
            orderdata.totalprice=int(pro.price)*int(request.session['qty'])
            orderdata.paytype=request.POST['paymentvia']
            if orderdata.paytype=='cod': 
                print(4444444444)
                orderdata.transaction_id='1234'
                orderdata.save()
                # return render(request,'checkout.html')
                return redirect('index')
            else:
                print(55555555555555)
                request.session['add']=request.POST ['add']
                request.session['add'] = request.POST['add']
                request.session['city'] = request.POST['city']
                request.session['state'] = request.POST['state']
                request.session['pin'] = request.POST['pin']
                request.session['amount'] = orderdata.totalprice 
                # return redirect('razorpay')
                return render(request,'checkout.html')
        else:
            print(77777777777777)
            return render(request,'checkout.html')
    else:
        print(888888888888888888888)
        return render(request,'checkout.html')

            

