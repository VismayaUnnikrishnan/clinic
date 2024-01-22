from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from health import models
from django.contrib.auth.models import User
from .models import Doctor,Patient,Login,Appointment
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
    return render(request,"index.html")

# def login(request):
#     return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def reg_doctor(request):
    return render(request,"doctor_reg.html")

def reg_pat(request):
    return render(request,"patient_reg.html")

def doctor_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        data = Doctor.objects.filter(user=user).values()
        return render(request, "doctor_dashboard.html", {'data': data})
    else:
        # Handle the case when the user is not authenticated
        # You might want to redirect them to the login page or handle it in your own way
        return render(request, "not_authenticated.html")



def patient_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        data = Patient.objects.filter(user=user).values()
        return render(request, "patient_dashboard.html", {'data': data})
    else:
        # Handle the case when the user is not authenticated
        # You might want to redirect them to the login page or handle it in your own way
        return render(request, "not_authenticated.html")
    

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def admn_doctor_view(request):
    data = Doctor.objects.all()
    print(data)
    return render(request,"admn_doctor_view.html",{'data':data})

def admin_patient_view(request):
    data = Patient.objects.all()
    print(data)
    return render(request,"admin_patient_view.html",{'data':data})

def admin_appointment(request):
    
        data = Appointment.objects.all().values()
        return render(request, "admin_appointment.html", {'data': data})


def admn_apnt_edit(request,apnt_id):
    Data = Appointment.objects.get(id=apnt_id)
    return render(request,'admin_appointment_edit.html',{'Data':Data})

   

def appointment_delete(request,ap_id):
    add = Appointment.objects.get(id=ap_id)
    add.delete()
    return redirect('admin_appointment')


def pt_delete(request,pnt_id):
    add = Patient.objects.get(id=pnt_id)
    add.delete()
    return redirect('admin_patient_view')


def doc_delete(request,doct_id):
    add = Doctor.objects.get(id=doct_id)
    add.delete()
    return redirect('admn_doctor_view')
    
    



def doctor_edit(request,doc_id):
    Data = Doctor.objects.get(id=doc_id)
    return render(request,'doctor_edit.html',{'Data':Data})


def add_doctor(request):
    
    if request.method == 'POST' and request.FILES:
        
        d_name = request.POST['d_name']
        d_email = request.POST['d_email']
        d_password = request.POST['d_password']
        d_username = request.POST['d_username']
        d_mobile = request.POST['d_mobile']
        d_image=request.FILES['d_image']
        d_special = request.POST['d_special']
        d_gender = request.POST['gridRadios']
        d_city = request.POST['d_city']
        d_state = request.POST['d_state']
        d_address = request.POST['d_address']
        d_code = request.POST['d_code']

        
        user = User.objects.create_user(username=d_username, email=d_email, password=d_password)

        
        doctor = Doctor.objects.create(
            user=user,
            d_name=d_name,
            d_email=d_email,
            d_password=d_password,
            d_username=d_username,
            d_mobile=d_mobile,
            d_image=d_image,
            d_special=d_special,
            d_gender=d_gender,
            d_city=d_city,
            d_state=d_state,
            d_address=d_address,
            d_code=d_code
        )
        doctor.save()

        return redirect('login_view')  # Redirect to the home page or any other page you desire

    return render(request, 'reg_doctor')  # Replace 'your_template.html' with the actual template you are using



def doctor_update(request,doc_id):
    if request.method=="POST":
        add=Doctor.objects.get(id=doc_id)
        add.d_name = request.POST['d_name']
        add.d_email = request.POST['d_email']
        add.d_password = request.POST['d_password']
        add.d_username = request.POST['d_username']
        add.d_mobile = request.POST['d_mobile']
        add.d_image=request.FILES['d_image']
        add.d_special = request.POST['d_special']
        add.d_gender = request.POST['gridRadios']
        add.d_city = request.POST['d_city']
        add.d_state = request.POST['d_state']
        add.d_address = request.POST['d_address']
        add.d_code = request.POST['d_code']
        add.save()
        return redirect("doctor_dashboard")
    

def doctor_appointment(request):
    data = Appointment.objects.all().values()
    return render(request,"doctor_appointment.html", {'data': data})



    
def patient_profile(request):
        if request.user.is_authenticated:
            user = request.user
            data = Patient.objects.filter(user=user).values()
            return render(request, "patient_profile.html", {'data': data})
        else:
            # Handle the case when the user is not authenticated
             # You might want to redirect them to the login page or handle it in your own way
            return render(request, "not_authenticated.html")
        

def add_patient(request):
    if request.method == 'POST' and request.FILES:
        p_name = request.POST['p_names']
        p_email = request.POST['p_email']
        p_password = request.POST['p_password']
        p_username = request.POST['p_username']
        p_mobile = request.POST['p_mobile']
        p_image=request.FILES['p_image']
        past_medical_history = request.POST.getlist('past_medical_history')
        p_gender = request.POST['gridRadioss']
        p_city = request.POST['p_city']
        p_state = request.POST['p_state']
        p_address = request.POST['p_address']
        p_code = request.POST['p_code']

        
        user = User.objects.create_user(username=p_username, email=p_email, password=p_password)

        
        patient = Patient.objects.create(
            user=user,
            p_name=p_name,
            p_email=p_email,
            p_password=p_password,
            p_username=p_username,
            p_mobile=p_mobile,
            p_image=p_image,
            past_medical_history=', '.join(past_medical_history),
            p_gender=p_gender,
            p_city=p_city,
            p_state=p_state,
            p_address=p_address,
            p_code=p_code
        )

        patient.save()

        return redirect('login_view')

    return render(request, 'reg_pat')  



def patient_edit(request, p_id):
    Data = Patient.objects.get(id=p_id)
    # Add your logic for handling the edit operation
    return render(request, 'patient_edit.html', {'Data': Data})




def patient_update(request,pt_id):
    if request.method=="POST":
        add=Patient.objects.get(id=pt_id)
        add.p_name = request.POST['p_names']
        add.p_email = request.POST['p_email']
        add.p_password = request.POST['p_password']
        add.p_username = request.POST['p_username']
        add.p_mobile = request.POST['p_mobile']
        add.p_image=request.FILES['p_image']
        add.past_medical_history = request.POST.getlist('past_medical_history')
        add.p_gender = request.POST['gridRadioss']
        add.p_city = request.POST['p_city']
        add.p_state = request.POST['p_state']
        add.p_address = request.POST['p_address']
        add.p_code = request.POST['p_code']
        add.save()
        return redirect("patient_profile")





@login_required
def patient_appointment(request):
    if request.method == 'POST':
        # Process form data and save to the database
        user_id = request.user.id  # Get the current user ID
        p_token = request.POST.get('p_token')
        p_name = request.POST.get('p_names')
        p_email = request.POST.get('p_email')
        p_mobile = request.POST.get('mobile')
        appointment_date = request.POST.get('appointmentDate') 
        selected_dpt = request.POST.get('selected_dpt')
        doctor_ap = request.POST.get('d_name')
        appointment_time = request.POST.get('appointment_time')

        appointment = Appointment(
            user_id=user_id,
            p_token=p_token,
            p_name=p_name,
            p_email=p_email,
            p_mobile=p_mobile,
            appointment_date=appointment_date,
            selected_dpt=selected_dpt,
            doctor_ap=doctor_ap,
            appointment_time=appointment_time
        )
        appointment.save()

        # You can add a success message or redirect to another page
        return redirect('patient_dashboard')

    # Render the form
    return render(request, 'patient_appointment.html', context={'Data': None})

def appointment_update(request, apt_id):
    if request.method == "POST":
        add = Appointment.objects.get(id=apt_id)
        add.p_token = request.POST['p_token']
        add.p_name = request.POST['p_names']
        add.p_email = request.POST['p_email']
        add.p_mobile = request.POST['mobile']  # Corrected field name
        add.appointment_date = request.POST['appointmentDate']  # Corrected field name
        add.selected_dpt = request.POST['selected_dpt']
        add.doctor_ap = request.POST['d_name']
        add.appointment_time = request.POST['appointment_time']
        add.save()
        return redirect("admin_appointment")


def patient_update(request,pt_id):
    if request.method=="POST":
        add=Patient.objects.get(id=pt_id)
        add.p_name = request.POST['p_names']
        add.p_email = request.POST['p_email']
        add.p_password = request.POST['p_password']
        add.p_username = request.POST['p_username']
        add.p_mobile = request.POST['p_mobile']
        add.p_image=request.FILES['p_image']
        add.past_medical_history = request.POST.getlist('past_medical_history')
        add.p_gender = request.POST['gridRadioss']
        add.p_city = request.POST['p_city']
        add.p_state = request.POST['p_state']
        add.p_address = request.POST['p_address']
        add.p_code = request.POST['p_code']
        add.save()
        return redirect("patient_profile")
    

def patient_noti(request):
    if request.user:
        user = request.user
        data = Appointment.objects.filter(user=user).values()
    
    return render(request, "patient_notification.html", {'data': data})


        


    

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Save login details in the Login table
            login_entry = Login.objects.create(user=user)
            print(f"Login entry created: {login_entry}")

            # Check if the user is a doctor
            if Doctor.objects.filter(user=user).exists():
                return redirect('doctor_dashboard')  # Redirect to doctor dashboard

            # Check if the user is a patient
            elif Patient.objects.filter(user=user).exists():
                return redirect('patient_dashboard')  # Redirect to patient dashboard

            # Check if the user is an admin
            elif user.is_staff:
               return redirect('admin_dashboard')
            # elif username == 'admin' and password == 'admin_password':
            #     return redirect('admin_dashboard')  # Redirect to admin dashboard

        else:
            # Handle invalid login credentials
            print("Invalid login credentials")
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')






