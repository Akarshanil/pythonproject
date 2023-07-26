from django.shortcuts import render,redirect
from newapp.models import addcategorydb,productdb
from website.models import contactdb,singupdb,cartmodel,admincart
from django.contrib import messages
from django.db import IntegrityError


# Create your views here.
def productwebsite(request):
    data=addcategorydb.objects.all()
    return render(request,"productsale.html",{"keye":data})

def aboutpage(request):
    return render(request,"aboutpage.html")
def productpage(request,catg):
    products=productdb.objects.filter(selectcategory=catg)
    return render(request,"productweb.html",{"pro":products})
def prodetailes(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"productdetailes.html",{"data":data})
def contactpage(request):
    return render(request,"contact.html")
def contactsave(request):
    if request.method=="POST":
        fir=request.POST.get('name')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        mess=request.POST.get('message')
        obj=contactdb(name=fir,email=em,number=ph,message=mess)
        obj.save()
    return  redirect(contactpage)
def signup(request):
    return render(request,"signup.html")
def signupsave(request):
    if request.method=="POST":
        use=request.POST.get('username')
        emm=request.POST.get('email')
        ps=request.POST.get('pass')
        repss=request.POST.get('re_pass')
        obj=singupdb(username=use,email=emm,password=ps,re_password=repss)
        obj.save()
    return  redirect(signin)
def signin(request):
    return render(request,"signin.html")
def userlogin(request):
    if request.method=="POST":
        usee=request.POST.get('your_name')
        pas=request.POST.get('your_pass')
        if singupdb.objects.filter(username=usee,password=pas).exists():
            request.session['username']=usee
            request.session['password']=pas
            return redirect(productwebsite)
        else:
            return redirect(signin)
    else:
        return redirect(signin)
def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(signin)
def cartsave(request,dataid):
    if request.method=="POST":
        pro=request.POST.get('productname')
        pri=request.POST.get('orginalprice')
        ou=request.POST.get('qunt')
        us=request.POST.get('use')
        obj=cartmodel(productname=pro,quantity=ou,price=pri,user=us)
        obj.save()
        messages.success(request, "Added To Cart")
    return redirect('prodetailes', dataid=dataid)
def cartpagesave(request):
    cartt=cartmodel.objects.filter(user=request.session['username'])
    return render(request,"cartpage.html",{"cart":cartt})


def checkoutpagelast(request,dataid):
    product=cartmodel.objects.filter(id=dataid)
    return render(request,"checkoutpage.html",{"pro":product})
def proadsave(request):
    if request.method=="POST":
        pro=request.POST.get('productname')
        ou=request.POST.get('qu')
        us=request.POST.get('use')
        pr=request.POST.get('price')
        firstn=request.POST.get('fistname')
        lastn=request.POST.get('lastname')
        country=request.POST.get('country')
        city=request.POST.get('city')
        pin=request.POST.get('pincode')
        ad=request.POST.get('address')
        a=request.POST.get('id')


        obj=admincart(productnm=pro,quantity=ou,price=pr,user=us,firstname=firstn,lastname=lastn,country=country,city=city,pincode=pin,address=ad,dataid=a)
        obj.save()
        messages.success(request, "Order successfully")
    return redirect(checkoutpagelast,dataid=a)


