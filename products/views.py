from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from .forms import ProductForm
from django.contrib.auth.models import User

def home(request):
    products = Product.objects.all
    return render (request, 'home.html',{'products':products})
@login_required
def create( request):
    form = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            
            title = request.POST.get('title')
            url = request.POST.get('url')
            body = request.POST.get('body')
            image = request.FILES.get('image')
            icon= request.FILES.get('icon')
            product = Product(title=title,url=url,body=body,image=image,icon=icon)
            product.save()
            return redirect ('/products/' + str(product.id) )
        else:
            return render (request, 'create.html',{'form':form})
    else:
        return render (request, 'create.html',{'form':form})
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id )
    
    return render (request, 'detail.html',{'product': product})
@login_required
def upvote(request, product_id):
    if request.method=='POST':
        
        product = get_object_or_404(Product, pk=product_id )
        product.votes_total +=1
        product.save()
        return redirect ('/products/' + str(product.id) )
    
    
