from django.shortcuts import render,HttpResponse,redirect
from .models import User,Author,Book   
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request,"index.html")
    # return HttpResponse("first page")

def registration(request):
    if request.method=='POST':
        if request.POST['select'] == 'Admin':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save
                return redirect(" ")
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            uname=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            image= request.POST['image']
            my_user=User.objects.create_user(first_name=firstname,last_name=lastname,username=uname,email=email,is_staff=False,is_superuser=True,imge=image)
            my_user.set_password(password)
            my_user.save()
        else:
            firstname=request.POST['first_name']
            lastname=request.POST['last_name']
            uname=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            image= request.POST['image']
            my_user=User.objects.create_user(first_name=firstname,last_name=lastname,username=uname,email=email,is_staff=True,is_superuser=False)
            my_user.set_password(password)
            my_user.save()
            
        return redirect("sign-in")
       
    return render(request,"registration.html")
 
def Author_input(request):
    if request.method=="POST":  
        name=request.POST['name']
        author_age=request.POST['age']
        birth_place=request.POST['birth_place']
        birth_date=request.POST['birth_date']
        death_date=request.POST['death_date']
        country=request.POST['country']
        author=Author(name=name,age=author_age,birth_place=birth_place,birth_date=birth_date,death_date=death_date,country=country)
        # print(author)
        author.save(Author)
        return redirect("Author_Input")
    return render(request,'Author_input.html')

# def sign_in(request):
    # return render(request,'sign-in.html')


def addbook(request):
    if request.method=="POST":
        bookname=request.POST['book_name']
        bookprice=request.POST['book_price']
        booklanguage=request.POST['book_language']
        booktype=request.POST['book_type'] 
        publishdate=request.POST['publish_date']
        book_image=request.POST['book_image']
        author = Author.objects.get(id=request.POST['author'])
        book=Book(author=author,book_name=bookname,book_price=bookprice,book_language=booklanguage,book_type=booktype,publish_date=publishdate,book_image=book_image,book_status=True)
        book.save()
        return redirect('Author_Input')
    all_author=Author.objects.all()
    return render(request,'addbook.html',{'all_author':all_author})

def admin_list(request):
    data=User.objects.filter(is_superuser=True)
    context={
        'data1': data
    }
    return render(request,'adminlist.html',context)

def staff_list(request):
    data=User.objects.filter(is_superuser=False)
    context={
        'data1': data
    }
    return render(request,'stafflist.html',context)


def author_list(request):
    data=Author.objects.filter()
    context={
        'data1': data
    }
    return render(request,'authorlist.html',context)

def book_list(request):
    data=Book.objects.filter()
    context={
        'data1': data
    }
    return render(request,'booklist.html',context)


def Forgot_Password(request): 
    return render(request,'auth-sign-up.html')


def Form_page(request):
    return render(request,'form-elements-component.html')





# first
# last
# user
# email
# password
# conform
# profile img
# user role(admin,staff)
# class Demo(View):
#     def get(self,request):
#         return val;
#     def post(self,request):
   