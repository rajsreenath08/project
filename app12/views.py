from django.shortcuts import render,redirect
from . models import SignUp
from . forms import SignUpForm,LoginForm,UpdateForm,ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            user=SignUp.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email already exists!!!")
                return redirect('/register')
            elif password!=confirmpassword:
                messages.warning(request,'Password not equal!!!')
                return redirect('/register')
            else:
                tab=SignUp(Name=name,Place=place,Email=email,Password=password,Photo=photo)
                tab.save()
                return redirect('/')
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=SignUp.objects.get(Email=email)
            if not user:
                messages.warning(request,'EMail doesnt exists!!')
                return redirect('/login')
            elif user.Password!=password:
                messages.warning(request,'Incorrect Password!!')
                return redirect('/login')
            else:
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
def home(request,id):
    user=SignUp.objects.get(id=id)
    return render(request,'home.html',{'user':user})
def update(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form = UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            name= form.cleaned_data['Name']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            form.save()
            messages.success(request,'Updated Successfully')
            return redirect('/home/%s' %user.id)
    else:
        form=UpdateForm(request.POST or None ,instance=user)
    return render(request,'update.html',{'user':user,'form':form})
def change_password(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST or None)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmnewpassword=form.cleaned_data['ConfirmNewPassword']
            if user.Password!=oldpassword:
                messages.warning(request,'Password incorrect!!!')
                return redirect('/change_password/%s' % user.id)
            elif newpassword!=confirmnewpassword:
                messages.warning(request,'Password doesnt match!!')
                return redirect('/change_password/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                return redirect('/')
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'user':user,'form':form})
def logout(request):
    logouts(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('/')
