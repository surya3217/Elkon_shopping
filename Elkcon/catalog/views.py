import email
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.http import HttpResponse
from .models import *
 
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'catalog/home.html',context)

def placeOrder(request,i):
    customer= Customer.objects.get(id=i)
    form=createorderform(instance=customer)
    if(request.method=='POST'):
        form=createorderform(request.POST,instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'catalog/placeOrder.html',context)
 
def addProduct(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'catalog/addProduct.html',context)
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else: 
        customerform=createcustomerform()
        if request.method=='POST':
            customerform=createcustomerform(request.POST)
            if customerform.is_valid():
                customer=customerform.save(commit=False)
                customer.save()
                return redirect('login')
        context={
            'customerform':customerform,
        }
        return render(request,'catalog/register.html',context)
 
def loginPage(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= Customer.objects.filter(email= email, password=password).first()
        print(user)
        if user is not None:
            return redirect('home')
        else:
            print('Please register first...')
    context={}
    return render(request,'catalog/login.html',context)
 
def logoutPage(request):
    request.session.flush()
    return redirect('login')
