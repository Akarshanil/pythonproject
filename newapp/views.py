from django.shortcuts import render,redirect
from newapp.models import addcategorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from website.models import contactdb,admincart
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def addcategory(request):
    return render(request,"AddCategory.html")
def categorysave(request):
    if request.method == "POST":
        na = request.POST.get('categoryname')
        da = request.FILES['image']
        ge = request.POST.get('description')

    obj = addcategorydb(categoryname=na, image=da, description=ge)
    obj.save()
    return redirect(addcategory)
def displaycategory(request):
    datab=addcategorydb.objects.all()
    return render(request,"DisplayCATEGORY.HTML.html",{"key":datab})
def editcategory(request,dataid):
    data=addcategorydb.objects.get(id=dataid)
    return render(request,"editsavecategory.html",{"kaya":data})
def updatecategory(request,dataid):
    if request.method=="POST":
        naa = request.POST.get('categoryname')
        gee = request.POST.get('description')
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
        addcategorydb.objects.filter(id=dataid).update(categoryname=naa,description=gee,image=file)
    except MultiValueDictKeyError:
        addcategorydb.objects.filter(id=dataid).update(categoryname=naa, description=gee)
    return redirect(displaycategory)
def deletecategory(request,dataid):
    databc=addcategorydb.objects.filter(id=dataid)
    databc.delete()
    return redirect(displaycategory)
def addproduct(request):
    databd=addcategorydb.objects.all()
    return  render(request,"Addproduct.html",{"keye":databd})
def productsave(request):
    if request.method=="POST":
        sele=request.POST.get('select_category')
        pro=request.POST.get('productname')
        qu=request.POST.get('quantity')
        pr=request.POST.get('price')
        des=request.POST.get('description')
        im=request.FILES['image']
        obj=productdb(selectcategory=sele,productname=pro,quantity=qu,price=pr,description=des,image=im)
        obj.save()
        messages.success(request,"the data is saved")
    return redirect(addproduct)
def  displayproduct(request):
    datasave=productdb.objects.all()
    return render(request,"displayproductsave.html",{"ke":datasave})
def editproctsavee(request,dataidd):
    product=addcategorydb.objects.all()
    databb=productdb.objects.get(id=dataidd)
    return render(request,"productedit.html",{"daa":databb, "pro":product})
def productupdate(request,dataidd):
    if request.method=="POST":
        selee = request.POST.get('select_category')
        proo = request.POST.get('productname')
        quu = request.POST.get('quantity')
        prr = request.POST.get('price')
        dess = request.POST.get('description')
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
        productdb.objects.filter(id=dataidd).update(selectcategory=selee,productname=proo,quantity=quu,price=prr,description=dess,image=file)
    except MultiValueDictKeyError:
        productdb.objects.filter(id=dataidd).update(selectcategory=selee, productname=proo, quantity=quu, price=prr,description=dess)
    messages.success(request, "the data is saved")
    return  redirect(displayproduct)
def deleteproduct(request,dataidd):
    data=productdb.objects.filter(id=dataidd)
    data.delete()
    messages.error(request, "the data is deleted")

    return redirect(displayproduct)

def adimloginpro(request):
      return render(request,"Adminlogin.html")
def loginprductt(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginprductt)
        else:
            return redirect(loginprductt)
def logoutproduct(request):
    del request.session['username']
    del  request.session['password']
    return redirect(adimloginpro)
def contactdisplay(request):
    data=contactdb.objects.all()
    return render(request,"contactdis.html",{"dat":data})
def deletecontact(request,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request, "the data is saved")

    return redirect(contactdisplay)
def orderuser(request):
    data=admincart.objects.all()
    return render(request,"displayordereduser.html",{"key":data})


