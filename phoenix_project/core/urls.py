from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('register_page/',register_page, name="register_page"),
    path('login_page/',login_page, name="login_page"),
    path('create',create,name="create"),
    path('retrieve',retrieve,name="retrieve"),
    path('edit/<int:id>',edit,name="edit"),
    path('update/<int:id>',update,name="update"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$',delete,name="delete"),  
]