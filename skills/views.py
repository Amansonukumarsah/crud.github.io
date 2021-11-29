from django.shortcuts import render

# Create your views here.
def skills(request):
    h={'skills':'active'}
    return render(request,'skills/skills.html',h)