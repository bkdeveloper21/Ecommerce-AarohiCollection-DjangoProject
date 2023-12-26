from django.db import models
from email import message
from django.contrib.auth.models import User


# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    email=models.EmailField(max_length = 254,default='SOME STRING')
    message=models.CharField(max_length=255,default='SOME STRING')
      

    def __str__(self):
        return self.name



CATEGORY_CHOICE=(
    ('Dress','Dress'),
    ('T-shirt','T-shirt'),
    ('Trouser','Trouser'),
    ('Jeans','Jeans'),
    ('Sweater','Sweater'),
    ('Jacket','Jacket'),
    ('shirt','shirt'),
    ('Coat','Coat'),
    ('Boot','Boot'),
    ('Bra','Bra'),
    ('Swimsuit','Swimsuit'),
    ('Gown','Gown'),
    ('Slip','Slip'),
    ('Wedding_dress','Wedding_dress'),
    ('Sport_bra','Sport_bra'),
    ('Shorts','Shorts'),
    ('hoodie','hoodie'),
    ('Gym_clothes','Gym_clothes'),
    ('Tank_top','Tank_top'),
    ('Long_coat','Long_coat'),
    ('Uniform','Uniform'),
    ('Dress_pants','Dress_pants'),
    ('Skirt','Skirt'),
    ('Hat','Hat'),
    ('Handbag','Handbag'),
    ('Scarf','Scarf'),
    ('Kurtas','Kurtas'),
    ('Lehenga_cholis','Lehenga_cholis'),
    ('Sarees','Sarees'),

)

SIZE_CHOICE=(
    ('XS','XS'),
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
    ('XXL','XXL'),
    ('XXXL','XXXL'),
    ('4XL','4XL'),
    ('5XL','5XL'),
    

)

STATE_CHOICES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))



class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    # category=models.ForeignKey('Category',on_delete=models.CASCADE)
    
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=14)
    product_image = models.ImageField(upload_to='product')
   # brand = models.CharField(max_length=200)
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE)
    #size = models.CharField(choices=SIZE_CHOICE,max_length=12)
    size = models.ForeignKey('Size',on_delete=models.CASCADE)
    #color = models.CharField(max_length=300)
    color = models.ForeignKey('Color',on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality =models.CharField(max_length=200,default='')
    city = models.CharField(max_length=50,default='pune')
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField(default=0)
    state = models.CharField(choices=STATE_CHOICES,max_length=100,default='Maharashtra')

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

STATUS_CHOICES =(
	('Accepted','Accepted'),
	('Packed','Packed'),
	('On The Way','On The Way'),
	('Delivered','Delivered'),
	('Cancel','Cancel'),
	('Pending','Pending'),
)



class Payment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	amount = models.FloatField()
	razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
	razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)	
	razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
	paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	orderd_date= models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
	payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
	@property
	def total_cost(self):
		return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     product = models.ForeignKey(Product,on_delete= models.CASCADE)
    

class Category(models.Model):
     category_name = models.CharField(max_length=200,default='')
     def __str__(self):
        return self.category_name
     
class Brand(models.Model):
     brand_name = models.CharField(max_length=200,default='')
     def __str__(self):
        return self.brand_name
     
class Size(models.Model):
     size = models.CharField(max_length=12,default='')
     title= models.CharField(max_length=20,default='XL')
     def __str__(self):
        return self.title
     
class Color(models.Model):
     color = models.CharField(max_length=300,default='')
     def __str__(self):
        return self.color