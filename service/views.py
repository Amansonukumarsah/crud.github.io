from django.shortcuts import render

# Create your views here.
def service(request):
    s={'service':'active'}
    return render(request,'service/service.html',s)