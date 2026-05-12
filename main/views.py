from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import AdForm, CommentForm
from unicodedata import category

from .models import Category, Advertisement, Comment

# Create your views here.

def home(request):
    categories=Category.objects.all()
    ads=Advertisement.objects.all()
    context={
        'categories':categories,
        'ads':ads
    }
    return render(request, 'main/index.html', context)

def ad_detail(request,ad_id):
    categories=Category.objects.all()
    ad=Advertisement.objects.get(pk=ad_id)
    context={
        'categories':categories,
        'ad':ad,
        'form':CommentForm()

    }
    return render(request, 'main/detail.html', context)

def ad_by_category(request,category_id):
    categories=Category.objects.all()
    ads=Advertisement.objects.filter(category_id=category_id)
    context={
        'categories':categories,
        'ads':ads,
    }
    return render(request, 'main/about.html', context)

def add_ad(request:HttpRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AdForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                ad = form.save()
                return redirect('detail', ad.id)
        else:
            form = AdForm()
        context = {
            'form': form
        }
        return render(request, 'main/add_ad.html', context)
    return redirect('home')

def update_ad(request:HttpRequest, ad_id:int):
    ad=Advertisement.objects.get(id=ad_id)
    if request.method=='POST':
        form=AdForm(data=request.POST, files=request.FILES, instance=ad)
        if form.is_valid():
            ad.save()
            return redirect('detail', ad_id=ad_id)

    form=AdForm(instance=ad)
    context={
        'form':form
    }
    return render(request, 'main/update_ad.html', context)

def delete_ad(request:HttpRequest, ad_id:int):
    ad=Advertisement.objects.get(id=ad_id)
    if request.method=='POST':
        ad.delete()
        return redirect('home')
    contwxt={
        'ad':ad
    }
    return render(request, 'main/confirm.html', contwxt)










