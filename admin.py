from django.contrib import admin
from .models import Doctor,Patient,Login,Appointment

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Login)
admin.site.register(Appointment)

