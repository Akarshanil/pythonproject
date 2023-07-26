from django.urls import path
from newapp import views


urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('categorysave/',views.categorysave,name="categorysave"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('productsave/', views.productsave, name="productsave"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproctsavee/<int:dataidd>/',views.editproctsavee, name="editproctsavee"),
    path('productupdate/<int:dataidd>/',views.productupdate, name="productupdate"),
    path('deleteproduct/<int:dataidd>/',views.deleteproduct, name="deleteproduct"),
    path('adimloginpro/',views.adimloginpro, name="adimloginpro"),
    path('loginprductt/',views.loginprductt,name="loginprductt"),
    path('logoutproduct/',views.logoutproduct,name="logoutproduct"),
    path('contactdisplay/',views.contactdisplay,name="contactdisplay"),
    path('deletecontact/<int:dataid>/', views.deletecontact, name="deletecontact"),
    path('orderuser/', views.orderuser, name="orderuser"),

]