from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import *
from base.models import cartmodel
import re
from django.contrib.auth.decorators import login_required


# Create your views here.
def valid_pasw(pasw):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern,pasw)

    
def register(request):
    if request.method=='POST':
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        uname =request.POST['uname']
        psw =request.POST['psw']
        try:
            u = User.objects.get(username = uname)
            return render(request,'register.html',{'erorr':'user name already exist'})
            
        except:
            if not valid_pasw(psw):
                messages.error(request,'the password must be strong')
                return redirect(register)

            u = User.objects.create_user(
                first_name=fname,
                last_name=lname,
                email=email,
                username=uname,
                password=psw,
            
        )
            u.set_password(psw)
            u.save()
            return redirect ('login_')
    return render(request,'register.html')
def login_(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        user= authenticate (username=uname,password=psw)
        
        if user:
            login(request,user)
            messages.success(request,'Login Successfully')
            return redirect('home')
        else:
            messages.error(request,'entered username or password is wrong...!')
            return redirect('login_')
    return render(request,'login_.html')
@login_required(login_url='login_')
def profile_(request):
    cart_products = cartmodel.objects.filter(host=request.user).count()
    data =profile.objects.filter(host=request.user).first()
    if not data:
        data=profile.objects.create(host=request.user)
    if request.method == 'POST':
        
        pimage = request.FILES.get('pimage')
        # data.delete()
        # profile.objects.get_or_create(
        #     pimage = pimage
        # )
        data.pimage = pimage
        data.save()

        

    return render(request,'profile_.html',{'data':data,'cart_products':cart_products})
def logout_(request):
   
    logout(request)
    messages.success(request,'Logout successfully')
    return redirect('login_')
def forget(request):
    if request.method == 'POST':
        if 'uname' in request.POST:
            uname = request.POST['uname']
            try:
               user = User.objects.get(username= uname)
               request.session['fp_user'] = user.username
               return render(request,'forgot.html',{'new':True})
          
            
            except:
                messages.error(request,'username does not exist !!.....')
                return redirect(forget)
        
    
        if 'new_pasw' in request.POST:
            user = request.session.get('fp_user')
            data = User.objects.get(username=user)

            new_pasw = request.POST['new_pasw']
            confirm_pasw = request.POST.get('confirm_pasw')

    
        if new_pasw == confirm_pasw:
            data.set_password(new_pasw)
            data.save()

            del request.session['fp_user']
            messages.success(request, 'Password reset successfully')
            return redirect('login_')
        else:
            messages.error(request, "Passwords do not match")
            return redirect(forget)
            
        
    return render(request,'forgot.html')
def reset_pasw(request):
    data = User.objects.get(username = request.user)
    if request.method == 'POST':
        if 'old_pasw' in request.POST:
            old_pasw =request.POST['old_pasw']

            a= authenticate(username = request.user,password = old_pasw)
            print(a)
            if a:
                return render(request,'reset.html',{'new':True})
            
            else:
                messages.error(request,'old password is wrong !!.....')
                return redirect('reset_pasw')
        if 'new_pasw' in request.POST:
            new_pasw = request.POST['new_pasw']
            data.set_password(new_pasw)
            data.save()
            messages.success(request,'password updated sucssesfully')
            return redirect(logout_)
    return render(request,'reset.html')
def update(request):
    data =request.user
    print(data.first_name)
    print(data.last_name)
    #data1=User.objects.get(username=request.user)
    if request.method=='POST':
        fname =request.POST['fname']
        lname =request.POST['lname']
        email =request.POST['email']
        uname =request.POST['uname']
        data.first_name = fname
        data.last_name = lname
        data.email = email
        data.username = uname
        data.save()
        return redirect('profile_')
    return render(request,'update.html',{'data1':data})
