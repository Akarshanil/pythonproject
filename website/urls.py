from django.urls import path
from website import views


urlpatterns=[
    path('productwebsite/',views.productwebsite,name="productwebsite"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('productpage/<catg>/',views.productpage,name="productpage"),
    path('prodetailes/<int:dataid>/',views.prodetailes,name="prodetailes"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('signup/', views.signup, name="signup"),
    path('signupsave/', views.signupsave, name="signupsave"),
    path('signin/', views.signin, name="signin"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartsave/<int:dataid>/', views.cartsave, name="cartsave"),
    path('cartpagesave/', views.cartpagesave, name="cartpagesave"),
    path('checkoutpagelast/<int:dataid>/', views.checkoutpagelast, name='checkoutpagelast'),
    path('proadsave/', views.proadsave, name="proadsave"),

]