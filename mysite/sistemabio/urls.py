
from django.urls import path

from . import views

app_name = "sistemabio"
urlpatterns = [
    path("",views.index, name="home"),
    path("signup/",views.signup, name="signup"),
    path("signin/",views.signin, name="signin"),
    path("logout/",views.signout,name="logout"),
    path("about/",views.about, name="about"),
    path("principal/",views.principal, name="principal"),

    #Inquilinos
    path("inquilinosinicial/", views.inquilinosinicial, name="inquilinosinicial"),
    path("inquilinos/",views.inquilinos, name="inquilinos"),
    path("new_inquilino/",views.new_inquilino, name="new_inquilino"),
    path("search_inquilino/",views.search_inquilino, name="search_inquilino"),
    # path("search_inquilino/<int:inquilino_para>",views.search_inquilino, name="search_inquilino"),
    path("detail_inquilino/<int:usuario_id>/",views.detail_inquilino, name ="detail_inquilino"),
    path("delete_inquilino/<int:inquilino_id>/", views.delete_inquilino, name="delete_inquilino"),
    

    #Visitantes

    #Trabajadores


    
] 
   