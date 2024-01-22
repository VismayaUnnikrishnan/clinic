"""
URL configuration for Clinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from health import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index,name="index"),
    path("login_view",views.login_view,name="login_view"),
    path("register",views.register,name="register"),
    path("reg_doctor",views.reg_doctor,name="reg_doctor"),
    path("reg_pat",views.reg_pat,name="reg_pat"),
    path("add_doctor",views.add_doctor,name="add_doctor"),
    path("add_patient",views.add_patient,name="add_patient"),
    path("doctor_dashboard",views.doctor_dashboard,name="doctor_dashboard"),
    path("patient_dashboard",views.patient_dashboard,name="patient_dashboard"),
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("admn_doctor_view",views.admn_doctor_view,name="admn_doctor_view"),
    path("admin_patient_view",views.admin_patient_view,name="admin_patient_view"),
    path("admin_appointment",views.admin_appointment,name="admin_appointment"),
    path("doctor_edit/<int:doc_id>",views.doctor_edit,name="doctor_edit"),
    path("doctor_update/<int:doc_id>",views.doctor_update,name="doctor_update"),
    path("patient_profile",views.patient_profile,name="patient_profile"),
    path("patient_edit/<int:p_id>", views.patient_edit, name="patient_edit"),
    path("patient_update/<int:pt_id>",views.patient_update,name="patient_update"),
    path("patient_appointment",views.patient_appointment,name="patient_appointment"),
    path("appointment_delete/<int:ap_id>", views.appointment_delete, name="appointment_delete"),
    path("pt_delete/<int:pnt_id>",views.pt_delete,name="pt_delete"),
    path("doc_delete/<int:doct_id>",views.doc_delete,name="doc_delete"),
    path("admn_apnt_edit/<int:apnt_id>",views.admn_apnt_edit,name="admn_apnt_edit"),
    path("appointment_update/<int:apt_id>",views.appointment_update,name="appointment_update"),
    path("patient_noti",views.patient_noti,name="patient_noti"),
    path("doctor_appointment",views.doctor_appointment,name="doctor_appointment"),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
