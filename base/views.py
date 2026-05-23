from django.shortcuts import render,redirect
from .models import productmodel,cartmodel
from django.db.models import Q
# Create your views here.
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    
    offer = False
    trend = False
    
    cart_products = cartmodel.objects.filter(host=request.user).count()
    q = request.GET.get('q')
    
    if q:
        all_products = productmodel.objects.filter(
            (Q(pname__icontains=q) | Q(pcategory__icontains=q)& Q(is_delete=False) ),
            
        )
        if len(all_products) == 0 :
            messages.error(request,'no products')
    elif 'cat' in request.GET :
        cat = request.GET['cat']
        print(cat)

        all_products = productmodel.objects.filter(Q(pcategory=cat)& Q(is_delete=False) )
    elif 'offer' in request.GET:
        all_products = productmodel.objects.filter(Q(offer = True)&Q(is_delete = False))
        offer = True
    elif 'trend' in request.GET:
        all_products = productmodel.objects.filter(Q(trending = True)&Q(is_delete = False))
        trend = True
    else:
        all_products = productmodel.objects.filter(is_delete=False)

   
    category = []
    data =  productmodel.objects.all()
    for i in data:
        if i.pcategory not in category:
            category += [i.pcategory]
        

    return render(request, 'home.html', {'all_products': all_products,'category':category,'offer':offer,'trend':trend,'nav':True,'cart_products':
    cart_products  })
@login_required(login_url='login_')
def cart (request):
    cart_products = cartmodel.objects.filter(host=request.user).count()
    cart_product = cartmodel.objects.filter(host=request.user) 
    TA = 0
    for i in cart_product :
        TA+=i.total_price
    return render(request,'cart.html',{'cart_product':cart_product,'TA':TA,'cart_products':cart_products})
@login_required(login_url='login_')
def addcart(request,pk):
    product = productmodel.objects.get(id=pk)
    try :
        cp = cartmodel.objects.get(pname = product.pname)
        cp.pqauntity+=1
        cp.total_price +=cp.price
        cp.save()
    except:    
            cartmodel.objects.create(
                pname= product.pname,
                price = product.price,
                pcategory  = product.pcategory ,
                total_price = product.price,
                host = request.user
        
    )
    return redirect('home')
def increase(request,pk):
    cp = cartmodel.objects.get(id=pk)
    cp.pqauntity+=1
    cp.total_price+=cp.price
    cp.save()
    return redirect('cart')
def decrease(request,pk):
    cp  = cartmodel.objects.get(id=pk)
    if cp.pqauntity > 1 :
        cp.pqauntity-=1
        cp.total_price-=cp.price
        cp.save()
    else:
        cp.delete()
    return redirect (cart)
def delete_(request,pk):
    cp = cartmodel.objects.get(id=pk).delete()
    return redirect(cart)

