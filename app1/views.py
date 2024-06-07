from django.shortcuts import render,HttpResponse,redirect
from  .models import Author,category,product,userRegister

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
        cpassword=request.POST['cpassword']
        userAlready=userRegister.objects.filter(email=request.POST['email'])
        if len(userAlready) > 0:
                    return render(request,"register.html",{'userAlready':'This email is already registered'})
        else:
              if cpassword!=request.POST['password']:
               return render(request,'register.html',{"passnotmatch":'Confirm password is not mathced!'})
              else:
               user.save()
              return render(request,"register.html",{'store':'You are registered Successfully'})
    else:
        return render(request,"register.html")
   
def Login(request):
#    try:
      if request.method=="POST":
        useremail=userRegister.objects.get(email=request.POST['email'])

        if useremail.password == request.POST['password']:
          return redirect("index")     
        else:
            return render(request,"login.html",{'pass':'Password is incorrect...'})
      else:
         return render(request,"Login.html")
#    except Exception as e:
    #  return render(request,"login.html",{'email':'email is incorrect...'})     
