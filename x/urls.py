
from django.urls import path

from x.views import home, login

urlpatterns = [

    path('', home, name="home"),
    path('login', login, name="login"),

]


