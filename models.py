from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    d_name = models.CharField(max_length=100)
    d_email = models.EmailField()
    d_password = models.CharField(max_length=100)
    d_username = models.CharField(max_length=50) 
    d_mobile = models.CharField(max_length=15)
    d_image = models.ImageField(upload_to="images")
    d_special = models.CharField(max_length=50)
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    d_gender = models.CharField(max_length=10, choices=gender_choices)
    d_city = models.CharField(max_length=50)
    d_state = models.CharField(max_length=50)
    d_address = models.TextField()
    d_code = models.CharField(max_length=10)

    def __str__(self):
        return self.d_name




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField()
    p_password = models.CharField(max_length=100)
    p_username = models.CharField(max_length=50)
    p_mobile = models.CharField(max_length=15)
    p_image = models.ImageField(upload_to="images")
    past_medical_history = models.CharField(max_length=100, blank=True, null=True)
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    p_gender = models.CharField(max_length=10, choices=gender_choices)
    p_city = models.CharField(max_length=50)
    p_state = models.CharField(max_length=50)
    p_address = models.TextField()
    p_code = models.CharField(max_length=10)

    def __str__(self):
        return self.p_name
    


class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    
    
    
    # Add any other fields you want to store, such as IP address, etc.

    def __str__(self):
        return f'{self.user.username} '




class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    p_token = models.CharField(max_length=5)
    p_name = models.CharField(max_length=255)
    p_email = models.EmailField()
    p_mobile = models.CharField(max_length=15)
    appointment_date = models.DateField()
    selected_dpt = models.CharField(max_length=255)
    doctor_ap = models.CharField(max_length=255)
    appointment_time =models.CharField(max_length=15)
    

    def __str__(self):
        return f'{self.p_name}'
    






