from . import views
from django.urls import path

urlpatterns = [
    path('', views.load_home , name='home'),
    path('about', views.load_about, name='about'),
    path('contact',views.laod_contact, name='contact'),
    path('why',views.load_why , name='why'),
    path('service',views.laod_service , name='service'),
    path('contact-form-submitted',views.form_data, name='contact-form-submitted'),
]