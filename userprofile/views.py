from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


from .models import Userprofile

from store.forms import ProductForm
from store.models import Product, Category

def vendor_detail(request,pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_detail.html', {
        'user':user
    })

@login_required
def my_store(request):
    return render(request, 'userprofile/my_store.html')

@login_required
def add_product(request):
    form = ProductForm()
    return render(request, 'userprofile/add_product.html', {
        'form': form,
    })

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form,
    })
