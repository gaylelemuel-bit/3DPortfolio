from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request,'pages/mission.html' )

def experience_view(request):
    return render(request,'pages/skills.html' )