
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# from whatsapp_chat.views import whatsapp_icon_view

urlpatterns = [
    path("",views.home,name='home'),
    path('contactus/', views.contactus, name='contactus'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('whatsapp/', views.whatsapp_icon_view, name='whatsapp-icon'),
    
    path('shippinganddeliverypolicy/', views.shippinganddeliverypolicy, name='shippinganddeliverypolicy'),
    path('termsandconditions/', views.termsandconditions, name='termsandconditions'),
    path('cancellationrefundpolicy/', views.cancellationrefundpolicy, name='cancellationrefundpolicy'), 
    path('basecopy/', views.basecopy, name='basecopy'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('aboutustest/', views.aboutustest, name='aboutustest'),
    path('login/', views.login, name='login_register'),
    path('registration/privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('refundpolicy/', views.refundpolicy, name='refundpolicy'),
    path('returnsexchangepolicy/', views.returnsexchangepolicy, name='returnsexchangepolicy'),
    path('termsandservices/', views.termsandservices, name='termsandservices'),
    path('registration/', views.registration, name='registration'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    # path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),

    path('product-size/<val>/', views.CategorySize.as_view(), name='category-size'),

    path('registration2/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
   
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/<int:prod_id>/', views.remove_cart, name='removecart'),
   # path('removecart/<int:prod_id>/', views.remove_cart, name='removecart'),
   # path('removecart/<int:prod_id>/', views.remove_cart, name='removecart'),
    
    path('pluswishlist/',views.plus_wishlist,name='pluswishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minuswishlist'),
    path('showwishlist/',views.show_wishlist,name='showwishlist'),
    path('search/',views.search,name='search'),
    path('test/',views.test,name='test'),
    

   

    #authentication
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchangedone.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page="login"), name='logout'),

    #password reset
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    



]

admin.site.site_header ="New Aarohi Collection (Admin dashboard)"
admin.site.site_title ="New Aarohi Collection"
admin.site.site_index_title ="New Aarohi Collection"
admin.site.app_index ="New Aarohi Collection"


