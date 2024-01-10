
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, timedelta
import random
from . import models 
from django.core.signing import Signer, BadSignature
from django.core.mail import send_mail
from django.utils.html import format_html
from . models import user_register



def user_index_panel(request):

    all_data = user_register.objects.all().order_by('pk')#this is acsending form align items #this is decending form order_py('-pk') 
    # all_user_data = user_register.objects.select_related('id').all()  #making a relation between our user model and role model by using select_related                          
    if (len(all_data)==0):
        status = False
    else:
        status = True

    # if (len(all_user_data)==0):
    #     user_status = False
    # else:
    #     user_status = True
    
    msg = messages.get_messages(request)
    data = {'all_data':all_data, 'status':status,'msg':msg}
    return render(request, 'naver/login.html', data)

# Create your views here.
def signup_auth_panel(request):
    if 'user_id' in request.session:
        return redirect('/register/signup/')
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email').strip()
        mobile = request.POST.get('mobile')
        # identy_no = request.POST.get('identy_no')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        e_pattern = r"^[a-zA-Z0-9_.]+@gmail\.com$"
        o_pattern = r"^[a-zA-Z0-9_.]+@(outlook\.com|hotmail\.com|live\.com)$"
        y_pattern = r"^[a-zA-Z0-9_.]+@yahoo\.com$"

        if any(len(value) == 0 for value in [fname, email, mobile, password, con_password]):
        # if any(value is None or len(value) == 0 for value in [ fname, email, mobile, identy_no, password, conpw]):
            messages.error(request, 'Empty field not accepted')

        else:
            if(len(fname)<3):
                messages.error(request, 'the field length must be minimum 3')
                return redirect('/register/signup/')
            elif(len(password)<8 ):
                messages.error(request, 'Password length must be minimum 8')
                return redirect('/register/signup/')
            elif(not re.search(r'[A-Z]', password)):
                messages.error(request, 'Password must contain at least one uppercase letter')
                return redirect('/register/signup/')
            elif(not re.search(r'\d', password)):
                messages.error(request, 'Password must contain at least one digit')
                return redirect('/register/signup/')
            elif(not re.search(r'[!@#$%^&*()_+=\-{}[\]:;"\'|<,>.?/~]', password)):
                messages.error(request, 'Password must contain at least one special character')
                return redirect('/register/signup/')
            elif(password!=con_password):
                messages.error(request, 'Your password and confirm password does not match.')
                return redirect('/register/signup/')
            elif(models.user_register.objects.filter(mobile=mobile).exists()):
                messages.info(request, 'Phone number already exists.')
                return redirect('/register/signup/')
            elif(len(mobile)!=11):
                messages.error(request, 'Phone number must be 11 digit.')
                return redirect('/register/signup/')
            # elif(models.user_register.objects.filter(identy_no=identy_no).exists()):
            #     messages.info(request, 'ID number already exists.')
            #     return redirect('/signup/')
            elif not re.match(e_pattern, email) and not re.match(o_pattern, email) and not re.match(y_pattern, email):
                messages.error(request, 'Email is not valid.')
                return redirect('/register/signup/')

            else:
            #   user_obj = User()
            #   user_obj = user_register.objects.get(id=id)
              v_key, link = email_generator(fname)
              
              # this is create method it's fast
              user_register.objects.create(fname=fname,email=email,mobile=mobile,password=password,v_key=v_key,v_status=0 )
              send_mail(f"Hello Mr. {fname} Please confirm your Registration in Doc.com",link,'maniruzzaman.manir96@gmail.com',[email],html_message=link)
            #   this is save method 
            # user_model = user_register()
            # user_model.fname = fname
            # user_model.email = email
            # user_model.mobile = mobile
            # user_model.identy_no = identy_no
            # user_model.password = password
            # # user_obj.id = user_id
            # user_model.save()
            
            messages.success(request, 'User Registration succesfully!')
            return redirect('/register/signup/')
    return render(request, 'naver/login.html')

def email_generator(fname):
    current_time = datetime.now().strftime("%H:%M:%S")
    h, m, s= map(int, current_time.split(':'))
    time_sec = h*3600 + m*60 + s
    time_sec = str(time_sec)

    random_number = random.choices('123456790',k=4)
    random_number = ''.join(random_number)
    v_c = time_sec + random_number
    
    signer = Signer()
    encrypted_value = signer.sign(v_c)
    encrypted_value1 = signer.sign(v_c).split(":")[1]
    decrypted_value = signer.unsign(encrypted_value)
    

    link = f"<p>Congratulations Mr {fname} ! For registering as a user in our doctor appointment system. To confirm the registration </p><a href='http://127.0.0.1:8000/register/email_verification/"+encrypted_value1+"' target='_blank'>please click this Activation link</a>"

    formatted_link = format_html(link)
    return encrypted_value1,formatted_link



def email_verify(request,id):
   
    v_key = id
    user = user_register.objects.get(v_key=v_key)
    user.v_status = 1
    user.save()
    user_data = {"u_data": user}

    return render(request, 'naver/congrats.html', user_data)


def login_auth_panel(request):
    google_data = request.session.get('social_auth_google-oauth2')
    if 'user_id' in request.session or google_data:
        print(1)
        return redirect('signup')
    
    else:
        print(2)
        google_data = request.session.get('social_auth_google-oauth2')
        print(google_data)
        if google_data:
            print(3)
            return redirect('signup')
        
        if request.method == 'POST':
            print(4)
            email = request.POST.get('email')
            password = request.POST.get('password')
            # user = None
            try:
                print(5)
                
                user = user_register.objects.get(email=email)
                print(user)


                if user.password==password:
                    print(6)
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    request.session['user_fname'] = user.fname
                    return redirect('checkout')
                else:
                    print(7)
                    # return HttpResponse("Login Failed")
                    messages.success(request, 'Wrong Password')
                    return redirect('/signup/')
            except user_register.DoesNotExist:
                
                messages.success(request, 'this user is not available')
                return redirect('/signup/')

                # user = authenticate(request, email=email, password=password)
                
                # if user:
                #     # login(request, user)
                #     return redirect('/hm/')
                
            
            # request.session['user_gid'] = google_data.uid
            # request.session['user_gemail'] = google_data.email
            
        else:
            return render(request, 'naver/login.html')



def logout_auth_panel(request):
    # Check if user is logged in
    if 'user_id' in request.session:
        # Clear session data
        request.session.flush()
        # messages.success(request, 'You have been logged out successfully.')
    if 'social_auth_google-oauth2' in request.session:
        del request.session['social_auth_google-oauth2']
    return redirect('home')
