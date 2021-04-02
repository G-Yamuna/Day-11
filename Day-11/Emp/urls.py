from django.urls import path
from Emp import views

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('contactus/',views.contact,name="ct"),
    path('login/',views.login,name="lg"),
    path('register/',views.register,name="rg"),
   
]