from django.shortcuts import render , redirect
from .models import Form
from django.views.decorators.csrf import csrf_protect

@csrf_protect

# Create your views here.
def load_home(request):
    return render(request, 'index.html')
def load_about(request):
    return render(request, 'about.html')
def laod_contact(request):
    return render(request,'contact.html')
def laod_service(request):
    return render(request,'service.html')
def load_why(request):
    return render(request,'why.html')
def form_data(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    phn = request.POST.get('phn')
    message = request.POST.get('message')

    print(email,phn,message)

    form = Form()
    form.fname = fname
    form.lname = lname
    form.email = email
    form.phn   = phn
    form.message = message
    form.save()
    return redirect('contact')