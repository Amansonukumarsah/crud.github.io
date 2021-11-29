from django.shortcuts import render

# Create your views here.
def home(request):
    h={'home':'active'}
    return render(request,'core/home.html',h)

def contact(request):
    c={'contact':'active'}
    return render(request,'core/contact.html',c)