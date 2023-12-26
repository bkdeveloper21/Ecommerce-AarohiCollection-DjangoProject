from ctypes.wintypes import HINSTANCE
from email import message
from itertools import count
from typing import Self
from django.db.models import Count
from django.core.validators import validate_email
from django.utils.datastructures import MultiValueDictKeyError


from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
import razorpay

from app.models import Customer,Product
from app.forms import CustomerForm, CustomerRegistrationForm,CustomerProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.core.mail import send_mail

#for html email start here
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.views import View

from . models import Cart, Customer, Enquiry, OrderPlaced, Product, Wishlist
from django.db.models import Q
from django.conf import settings
from razorpay import Payment



# Create your views here.
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render (request,"app/index.html",locals())

def basecopy(request):
    return render (request,"app/base copy.html")

def cancellationrefundpolicy(request):
    return render (request,"app/cancellationrefundpolicy.html")

def termsandconditions(request):
    return render (request,"app/termsandconditions.html")

def aboutus(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render (request,"app/aboutus.html",locals())

class CategoryView(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        size=Product.objects.filter(category=val).values('size')
        return render(request,"app/category.html" ,locals())
    
# def category(request):
#     sort_by = request.GET.get('sort_by')
    
    # if sort_by == 'brand':
    #     products = Product.objects.order_by('brand')
    # elif sort_by == 'size':
    #     products = Product.objects.order_by('size')
    # elif sort_by == 'price':
    #     products = Product.objects.order_by('price')
    # else:
    #     products = Product.objects.all()
    
    # context = {'products': products}
    # return render(request, 'category.html', context)
    
class CategoryTitle(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html" ,locals())
    

class CategorySize(View):
    def get(self,request,val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product=Product.objects.filter(size=val)
        
        size=Product.objects.filter(category=product[0].category).values('size')
        return render(request,"app/category.html" ,locals())
    
class ProductDetail(View):
    def get(self,request,pk):
        product =Product.objects.get(pk=pk)
        val=product.category #for getting category of object
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))

        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html" ,locals())

  
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/registration.html" ,locals())
        print("1")
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        print("2")
        if form.is_valid():
            print("3")
            form.save()
            #messages.SUCCESS(request,'good')
            messages.success(request, 'Congratulation! user Register successfully.')
        else:
            print("4")
            # messages.WARNING(request,'bad')
            messages.warning(request, 'Inavalid Input Data.')
        #return render(request,"app/customerregistrationform.html" ,locals())
        return render(request,"app/registration.html" ,locals())
    
@method_decorator(login_required,name='dispatch')  
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request,"app/profile.html" ,locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user =request.user
            name = form.cleaned_data['name']
            locality =form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile =form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode =form.cleaned_data['zipcode']

            reg =Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            print("-----------customer detailes save successfuly.----------------")
            messages.success(request, 'Congratulation! Profile Save successfully.')
        else:
            messages.warning(request, 'Inavalid data')
        return render(request,"app/profile.html" )

@login_required 
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render (request,"app/address.html",locals())

@method_decorator(login_required,name='dispatch')
class updateAddress(View):
    def get(self,request,pk):
        add= Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add= Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality =form.cleaned_data['locality']
            add.mobile =form.cleaned_data['mobile']
            add.city = form.cleaned_data['city']
            
            add.state = form.cleaned_data['state']
            add.zipcode =form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Congratulation! Profile Save successfully.')
        else:
            messages.success(request, 'eroor! .')
        return redirect('address')

def aboutustest(request):
    return render (request,"app/aboutustest.html")

def admin_dashboard(request):
    return render (request,"/admin/")

# def login(request):
    
    
#     return render (request,"app/login.html")
# return the view for the admin section


def login(request):
    return render (request,"admin/login")

def privacypolicy(request):
    return render (request,"app/privacypolicy.html")

def test(request):
    return render (request,"app/test.html")

def registration(request):
    return render (request,"app/registration.html")

def forgotpassword(request):
    return render (request,"app/forgotpassword.html")

def refundpolicy(request):
    return render (request,"app/refundpolicy.html")

def termsandservices(request):
    return render (request,"app/termsandservices.html")

def contactus(request):

    try:

        if request.method == 'POST':
            studForm = CustomerForm(request.POST)
            print("POST")
            if studForm.is_valid():
                print("Valid data")
                n = studForm.cleaned_data['name']
                mno = studForm.cleaned_data['mobileno']
                eml = studForm.cleaned_data['email']
                msg = studForm.cleaned_data['message']
                print(n + " "+mno+" "+eml+" "+msg)
                
                #sendMassEmail(request,eml)
                #sendSimpleEmail(request,eml)
                
          
                send_mail(
                'noreplynewaarohicollection',
                'Dear '+n+',\nThank you for choosing New Aarohi Collection for buy online clothes... I have received your Enquiry..as soon as possible we will contact to you\n\n\n\n Thanks and regards,\n Aarohi Collection\n Mobile no: 9604802874\n email: newaarohicollection@gmail.com ',
                'balajikaragir07@gmail.com',
                [eml],
                fail_silently=False,
                )

                send_mail(
                'enquiry',
                'ENQUIRY \n\n Name:'+n+'\n Mobile no:'+mno+'\n Email:'+eml+'\n Message:'+ msg+'',
                'balajikaragir07@gmail.com',
                ['karagirbalaji992@gmail.com'],
                fail_silently=False,
                )

               


                #whatsappdata(mno,msg)
                #successmsg = "Message has successufully sent..."
            # print(successmsg)
                # insert
                rec = Enquiry(name=n, mobileno=mno, email=eml, message=msg)
                rec.save()
                messages.success(request, 'Message has send successfully.')
                print("Alert message show succesufully")
                # update
                #rec = Student(2,name=n,roll=r,per=p)
                # rec.save()

                # delete

                print("Record Inserted Successfully")
                return redirect('contactus')
                #return redirect('customerinfo')

               # return render(request,'customerinfo')
            else:
                print("Invalid data")
                messages.error(request, 'Invalid credentials.')
        else:
             totalitem = 0
             wishitem = 0
             if request.user.is_authenticated:
                totalitem =len(Cart.objects.filter(user=request.user))
                wishitem = len(Wishlist.objects.filter(user=request.user))
             studForm = CustomerForm()
             print("GET")
            #rec = Customer(name=n,mobileno=mno,email=eml,message=msg)
            # rec.save()
        #return redirect('home')
        return render(request, "app/contactus.html", locals())
        # ret
        # urn render(request, "user/contactus.html")
    except Exception as e:
        raise e('error occure because data is not valid')
    
@login_required 
def add_to_cart(request):
    user= request.user
    product_id= request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user= user,product = product).save()
    return redirect("/cart")


@login_required 
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/addtocart.html',locals())

@login_required 
def show_wishlist(request):
    user = request.user
    # wishlist = Wishlist.objects.filter(user=user)
    # amount = 0
    # for p in wishlist:
    #     value = p.quantity * p.product.discounted_price
    #     amount = amount + value
    # totalamount = amount + 40
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request,'app/wishlist.html',locals())

@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem =len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount =famount + 40
        razoramount= int(totalamount * 100)
        client =razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data ={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        #{'id': 'order_M6FNT8zcG1VJ1A', 'entity': 'order', 'amount': 3900000, 'amount_paid': 0, 'amount_due': 3900000, 'currency': 'INR', 'receipt': 'order_rcptid_12', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': [], 'created_at': 1687714502}
        order_id = payment_response['id']
        order_status = payment_response['status']
           
        '''if order_status == 'created':
            payment = Payment(
                user=user,
                amount= totalamount,
                razorpay_order_id= order_id,
                razorpay_payment_status = order_status
            )
            payment.save()'''
      
      
        return render(request,'app/checkout.html',locals())

@login_required 
def payment_done(request):
    order_id=request.GET.get('order_id')
    payment_id=request.GET.get('payment_id')
    cust_id=request.GET.get('cust_id')
    

    # cust_id=request.GET.get('cust_id')
    user=request.user
    customer=Customer.objects.get(id=cust_id)
    payment=Payment.objects.get(razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity,payment=payment).save()
        c.delete()
    return redirect("orders")

@login_required 
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user)) 
        wishitem = len(Wishlist.objects.filter(user=request.user))    
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',locals())

@login_required 
def plus_cart(request):
    if request.method =="GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart= Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        print(prod_id)
        data={
            'quantity' :c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)

@login_required 
def minus_cart(request):
    if request.method =="GET":
        prod_id = request.GET['prod_id']
       # prod_id= 2
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart= Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40
        print(prod_id)
        data={
            'quantity' :c.quantity,
            'amount' : amount,
            'totalamount' : totalamount
        }
        return JsonResponse(data)

# @login_required 
# def remove_cart(request):
#     if request.method =="GET": 
#         prod_id= request.GET['prod_id']
        
#         print("this is product id which want to delet",prod_id)
#         c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
#         c.delete()
        
#         user = request.user
#         cart= Cart.objects.filter(user=user)
#         amount = 0
#         for p in cart:
#             value = p.quantity * p.product.discounted_price
#             amount = amount + value
#         totalamount = amount + 40
#         print(prod_id)
#         data={
            
#             'amount' : amount,
#             'totalamount' : totalamount,
#         }
#         # print(JsonResponse)
#         return JsonResponse(data)





@login_required 
def remove_cart(request, prod_id):
    if request.method == "GET": 
        prod_id = request.GET.get('prod_id')  # Use get() method to retrieve the value

        if prod_id is not None:
            # Check if 'prod_id' is not None before proceeding
            c = Cart.objects.filter(Q(product=prod_id), Q(user=request.user)).first()

            if c is not None:
                # Check if the cart item is found before deleting
                c.delete()

                user = request.user
                cart = Cart.objects.filter(user=user)
                amount = 0
                for p in cart:
                    value = p.quantity * p.product.discounted_price
                    amount = amount + value
                totalamount = amount + 40

                data = {
                    'amount': amount,
                    'totalamount': totalamount,
                }
                return JsonResponse(data)
            else:
                # Return a response if the cart item with the given 'prod_id' is not found
                data = {
                    'error': 'Cart item with the given prod_id not found.'
                }
                return JsonResponse(data, status=404)
        else:
            # Return a response if 'prod_id' is not provided in the GET request
            data = {
                'error': 'Invalid request. Missing prod_id parameter.'
            }
            return JsonResponse(data, status=400)




        
@login_required 
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save() 
        data={
            'message':'wishlist Added Successfuly.',
        }
        return JsonResponse(data)

@login_required    
def minus_wishlist(request):
    if request.method == 'GET':
        # product_id= request.GET.get('prod_id')
        prod_id = request.GET['prod_id']
       # prod_id = request.get('prod_id')
        product= Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete() 
        data={
            'message':'wishlist Remove Successfuly.',
        }
        return JsonResponse(data)

def search(request):
    query= request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem =len(Cart.objects.filter(user=request.user)) 
        wishitem = len(Wishlist.objects.filter(user=request.user))    
    product = Product.objects.filter(Q(title__contains=query))
    return render(request, 'app/search.html',locals())


def returnsexchangepolicy(request):
    return render(request, 'app/returnsexchangepolicy.html',locals())

def shippinganddeliverypolicy(request):
    return render(request, 'app/shippinganddeliverypolicy.html',locals())

def whatsapp_icon_view(request):
    return render(request, "app/whatsapp_icon.html",locals())