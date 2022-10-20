

from urllib import request
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth import authenticate , login as userlogin ,logout
from myapp.models import RegisterForm
from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request,'base.html')
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form":form
        }
        return render(request,'registration/login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                userlogin(request,user)
                return redirect('/')
        else:
            context = {
                "form":form
            }
            return render(request,'registration/login.html',context)






def index(request):
        brand= Brand.objects.all()
        category= Category.objects.all()
        brandId = request.GET.get('brand')
        CategoryId = request.GET.get('category')
        if CategoryId:
            product = Product.objects.filter(sub_category=CategoryId).order_by('-id')
        elif brandId:
            product = Product.objects.filter(brand=brandId).order_by('-id')

        else:
            product=Product.objects.all()

        context={
            "category":category,
            "brand":brand,
            "product":product
        }
        return render(request,'index.html',context)
def sign(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                ueername = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            
    else:
        form = RegisterForm()
    context = {
        "form":form
       }
        
    return render(request,'registration/signup.html',context)


##
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
####cart



@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def contect(request):
    if request.method =="POST":
        contect = contect_us(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contect.save()
    return render(request,'contect.html')
def checkoutview(request):
    if request.method =="POST":
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        
        for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total = a * b
            order =Order(
               
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                user=user,
                address=address,
                pincode=pincode,
                phone=phone,
                total=total

            )
            order.save()
        request.session['cart']={}
        return redirect('index')
        print(i)
           
        
        # print(phone,pincode,address,cart,user)
        
    return HttpResponse("this is check out page")
def yourorderview(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)
    # order=Product.objects.all()
    context = {
        'order':order
    }
    return render(request,'your_order.html',context)

def productpageview(request):
    brand= Brand.objects.all()
    category= Category.objects.all()
    brandId = request.GET.get('brand')
    CategoryId = request.GET.get('category')
    if CategoryId:
        product = Product.objects.filter(sub_category=CategoryId).order_by('-id')
    elif brandId:
        product = Product.objects.filter(brand=brandId).order_by('-id')

    else:
        product=Product.objects.all()

    context={
            "category":category,
            "brand":brand,
            "product":product
        }
    return render(request,'productpage.html',context)
def product_detailview(request,id):
    product=Product.objects.filter(id=id).first()

    context={
           
            "product":product
        }
    return render(request,'product_detail.html',context)
def searchview(request):
    query = request.GET['query']
    product=Product.objects.filter(name__icontains=query)

    context={
           
            "product":product
        }
    return render(request,'search.html',context)