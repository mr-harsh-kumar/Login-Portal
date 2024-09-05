from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as django_logout
# from django_project_2 import settings
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.hashers import make_password, check_password
from .models import My_Users
from django.contrib.staticfiles import finders
import os

# Create your views here.


def log(request):
    print("Welcome")
    base_dir = settings.BASE_DIR
   
    print("Base directory:", base_dir)
    print("Welcome")
    return HttpResponse("yo")


def home(request):
    return render(request, 'home.html')
    

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
    
def user_registeration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        
                       
        if My_Users.objects.filter(email=email):
            messages.warning(request,"Email alreday exists !!")
            return redirect('/login_system/register')
        
        if My_Users.objects.filter(username=username):
            messages.warning(request,"Username alreday exists !!")
            return redirect('/login_system/register')
            
            
            
        if len(username)<4:
            messages.warning(request,"Username is too small !!")
            return redirect('/login_system/register')
            
            
            
        if not username.isalnum() :
            messages.warning(request,"Enter a valid username !!")
            return redirect('/login_system/register')
            
        if password != confirm_password :
            messages.warning(request,"Passwords do not match !!")
            return redirect('/login_system/register')
            
            
            
            
        # Hash the password before saving it
        hashed_password = make_password(password)
        users = My_Users.objects.create(username=username, email=email, password=hashed_password)
        # users.save()
        messages.success(request,"You are registered now !!")
        
        print(email)
        print("working")
        mail(request,email)
        print("working")
            
            
        return redirect('/login_system/login')




def mail(request, email):
    try:
        subject = "HARSH KUMAR : A Full Stack Developer with Expertise in Django"
        message = '''I have a robust background in developing web applications using Django, a powerful framework for building scalable and secure web solutions. With my expertise in both front-end and back-end development, I can successfully delivered projects that meet client requirements and industry standards.

Here are some highlights of my skills and experience:

- Proficiency in Django framework for rapid and efficient development of web applications.
- Strong knowledge of front-end technologies such as HTML, CSS, JavaScript, and responsive design principles.
- Experience in database management and integration using Django ORM and other tools.
- Ability to work collaboratively in agile environments, ensuring timely delivery and high-quality code.
- Continuous learning and adaptation to new technologies and best practices in web development.
    
I am actively seeking new opportunities to contribute my skills and expertise to innovative projects and teams. I am passionate about creating robust and user-friendly web solutions that drive business growth and customer satisfaction.

'''
        from_email = settings.EMAIL_HOST_USER
        to_email = email
        email_message = EmailMessage(subject, message, from_email, [to_email])

        # Construct the file path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, 'static')

        # Attach the file to the email message
        if os.path.exists(file_path):
            email_message.attach_file(os.path.join(file_path,'Harsh_Resume.pdf'))
        else:
            print("File 'Harsh_Resume.pdf' not found.")

        email_message.send()
    except Exception as e:
        print("Error:", e)
        
def user_authentication(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        print("Username:", uname)
        print("Password:", passw)
        
        # Use filter to get users with matching username and password
        users = My_Users.objects.filter(username=uname)
        print("Authenticated User:", users)
        
        if users.exists():
            # If any users match the filter, log in the first user found
            
            user = users.first()
            if check_password(passw, user.password):
                # login(request)
                request.session['username'] = user.username
                messages.success(request,"successfully logged in")
                return redirect('/login_system/home')
                
                # return render(request,'home.html', {'username': uname})
        else:
            messages.warning(request, "Invalid credentials!")
            return redirect('/login_system/login')

    return render(request, 'login.html')


def logout(request):
    if 'username' in request.session:
        del request.session['username']
        messages.success(request, "You logged out successfully !!")
    return redirect('/login_system/login')
