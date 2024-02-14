from django.shortcuts import render
from .models import Register
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fName']
            lName=form.cleaned_data['lName']
            age=form.cleaned_data['age']
            email=form.cleaned_data['email']
            gender=form.cleaned_data['gender']
            Register.objects.create(firstName=fname,lastName=lName,age=age,email=email,gender=gender)
    f=RegisterForm()
    return render(request,'register.html',context={'form':f})

