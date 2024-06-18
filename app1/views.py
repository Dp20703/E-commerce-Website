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
        print(11111111111)
        user=userRegister.objects.get(email=request.session['email'])
        pro=product.objects.get(id=int(request.session['proid']))
        orderid=random.randint(0000000,9999999)
        print(22222)
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
                request.session['add'] = request.POST['add']
                request.session['city'] = request.POST['city']
                request.session['state'] = request.POST['state']
                request.session['pin'] = request.POST['pin']
                request.session['amount'] = orderdata.totalprice 
                return redirect('razorpay')
                
        else:
            print(77777777777777)
            return render(request,'checkout.html')
    else:
        print(888888888888888888888)
        return render(request,'checkout.html')
    

import razorpay

# RAZOR_KEY_ID ='rzp_test_6B4TAHm7KgY6Xd'
# RAZOR_KEY_SECRET = 'SDI7uApXtR6Vy7xHR5hcBNfd'
#mam
RAZOR_KEY_ID = 'rzp_test_7OImT75w0b3T5s'
RAZOR_KEY_SECRET = '2DyOadFeAUMu9vGCg2RFMXKj'

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(RAZOR_KEY_ID,  RAZOR_KEY_SECRET))


def razorpaymet(request):
    currency = 'INR'
    amount =  int(request.session['amount']) * 100   # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000//paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'razorpay.html', context=context)           


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request): 
 try:

    print(111111)
    amount = int(request.session['amount']) * 100
    # only accept POST request.
    if request.method == "POST":
            print(22222) 
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
              
            try:
                    print(333333333)
                # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    print("amount is error")
                    user = userRegister.objects.get(email = request.session['email'])
                    orderdata = order()
                    orderdata.userid = user.pk
                    orderdata.proid = request.session['proid']
                    orderdata.add = request.session['add']
                    orderdata.city = request.session['city']
                    orderdata.state = request.session['state']
                    orderdata.pincode = request.session['pin']
                    orderdata.qty = request.session['qty']
                    orderdata.orderid = razorpay_order_id
                    orderdata.totalprice = request.session['amount']
                    orderdata.paytype = "online"
                    orderdata.transaction_id = payment_id
                    orderdata.save()
                
                    # render success page on successful caputre of payment
                    # return render(request, 'paymentsuccess.html')
                    print(4444444444444)
                    return HttpResponse( 'payment successfull')
            except:
                    print(55555555555)
                    return HttpResponseBadRequest()
    else:
        print(6666666666666666)
       # if other than POST request is made.
        return HttpResponseBadRequest()
 except:
    print("final error")
    return redirect('index')