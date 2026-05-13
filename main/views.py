from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import AdForm, CommentForm
from django.contrib.auth.decorators import login_required
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
    comments=Comment.objects.filter(ad=ad).order_by('-created')
    context={
        'categories':categories,
        'ad':ad,
        'form':CommentForm(),
        'comments':comments

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

@login_required(login_url='home')
def save_comment(request:HttpRequest, ad_id:int):
    ad=Advertisement.objects.get(id=ad_id)
    if request.method=="POST":
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.ad=ad
            comment.user=request.user
            comment.save()
    return redirect('detail', ad_id=ad.pk)

@login_required(login_url='home')
def update_comment(request:HttpRequest, ad_id:int, comment_id:int):
    comment=Comment.objects.get(id=comment_id, ad_id=ad_id)
    context={}
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(data=request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('detail', ad_id=ad_id)
        context['form']=CommentForm(instance=comment)

    return render(request, 'main/update_comment.html', context)

@login_required(login_url='home')
def delete_comment(request, comment_id:int):
    comment=Comment.objects.get(pk=comment_id)
    if comment.user == request.user or request.user.is_superuser:
        if request.method =='POST':
            ad_id=comment.ad.pk
            comment.delete('detail', ad_id=ad_id)
            return redirect('')
        return render(request, 'main/confirm_delete_comment.html', )
    else:
        return redirect('home')













