from django.shortcuts import render,redirect

from .models import Register
from .forms import RegisterForm
from django.db import IntegrityError

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")
    
def contact(request):
    return render(request,"contact.html")

def userhome(request):
    return render(request,"userhome.html")

def adminhome(request):
    return render(request,"adminhome.html")

"""
def doregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Registration successful, redirecting to login.")
                return redirect('login')  # Ensure this is the correct URL name
            except IntegrityError as e:
                print(f"IntegrityError: {e}")
                if 'email' in str(e):
                    form.add_error('email', 'This email is already registered.')
                if 'password' in str(e):
                    form.add_error('password', 'This password is already in use.')
                if 'contact' in str(e):
                    form.add_error('contact', 'This contact number is already registered.')
        else:
            print("Form is not valid.")
            return render(request, "register.html", {'form': form})
    else:
        form = RegisterForm()
    return render(request,"register.html",{"form":form})
"""
def doregister(request):
    if request.method=='POST':
        hospitalname=request.POST['HospitalName']
        contact=request.POST['Phoneno']
        email=request.POST['Mail']
        password=request.POST['Password']
   # department=request.GET['department']
        branchaddress=request.POST['branchaddress']
   # UMR=request.GET['UMR']
    #doctor=request.GET['doctor']

    user=Register.objects.filter(email=email)
    if user:
        message= "User Already Exists"
        return render(request,"register.html",{'msg':message})
    else:
        r=Register()
        r.contact=contact
        r.hospitalname=hospitalname
        r.email=email
        r.branchaddress=branchaddress    
        r.password=password
   # r.UMR=UMR
        r.save()
        return render(request,"login.html",{'email':email})
    """  
    hospitalname=request.GET['HospitalName']
        contact=request.GET['Phoneno']
        email=request.GET['Mail']
        password=request.GET['Password']
   # department=request.GET['department']
        branchaddress=request.GET['branchaddress']
   # UMR=request.GET['UMR']
    #doctor=request.GET['doctor']
    
    
    r=Register()
    r.contact=contact
    r.hospitalname=hospitalname
    r.email=email
    r.branchaddress=branchaddress    
    r.password=password
   # r.UMR=UMR
    r.save()
    return render(request,"login.html",{"email":email})

"""
def logincheck(request):
    email=request.GET['Mail']
    password=request.GET['Password']
    #department=request.GET['department']
    #hospitalname=request.GET['HospitalName']
    #contact=request.GET['Phoneno']
   # r=None
    try:
        r=Register.objects.get(email=email,password=password)
    #    print("r=",r)
    except Exception as ex:
   #     print(ex)where 
        return render(request,"login.html",{"msg":"Invalid Designation"})
    #if(r!=None):
     #   if(r.design=="user"):
      #      return redirect("/userhome")
       # if(r.design=="admin"):
        #    return redirect("/adminhome")
    #else:
     #   return render(request,"login.html",{"msg":"Invalid Designation"})
    #r=Register.objects.get(email=email)
    return render(request,"room.html")
    

def action(request):
    email=request.GET['Mail']
    #firstname=request.GET['firstname']
    subject=request.GET['subject']
    hospitalname=request.GET['HospitalName'] 
    contact=request.GET['Phoneno']
    
    r=Register()
    r.email=email
    #r.firstname=firstname
    r.subject=subject
    r.hospitalname=hospitalname
    r.contact=contact
    r.save()
    return render(request,"contact.html",{"msg":"Successfully Submitted"})

# Create your views here.

def viewuser(request):
    #all() returns all rows in an table as a register class objects
    user=Register.objects.all()
    return render(request,"viewuser.html",{"user":user})


def modify(request):
    operations=request.GET['operations']
    print(operations)
    hospitalname=request.GET['HospitalName']
    contact=request.GET['Phoneno']   
    email=request.GET['email']
    password=request.GET['Password']
   # department=request.GET['department']
    branchaddress=request.GET['Branchaddress']
    design=request.GET['design']
    #doctor=request.GET['doctor']
    r=Register.objects.get(email=email)
   
    if operations=="update":
        r.contact=contact
        r.hospitalname=hospitalname
        r.email=email
        r.branchaddress=branchaddress    
        r.password=password
        r.design=design
        r.save()

    else:
      #  email=request.GET['Mail']  
      #  r=Register.objects.get(email=email) 
        Register.delete(r)     

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success_page')  # Redirect to a success page
            except IntegrityError as e:
                if 'email' in str(e):
                    form.add_error('email', 'This email is already registered.')
                if 'password' in str(e):
                    form.add_error('password', 'This password is already in use.')
                if 'contact' in str(e):
                    form.add_error('contact', 'This contact number is already registered.')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



    user=Register.objects.all()
    return render(request,"viewuser.html",{"user":user})