from django.shortcuts import render
from django.views.generic import TemplateView
   

# Create your views here.
class Home(TemplateView):
    def get(self,request):
        return render(request,'home.html')

def about_us(request):
    return render(request,'about_us.html')

def contact_us(request):
    return render(request,'contact_us.html')

def beginner_to_pro(request):
    return render(request,'beginner_to_pro.html')

def fast_track_training(request):
    return render(request,'fast_track_training.html')

def workshops(request):
    return render(request,'workshops.html')

def live_session(request):
    return render(request,'live_session.html')

def skill_to_trainer(request):
    return render(request,'skill_to_trainer.html')

def ultimage_trainer_launch_pack(request):
    return render(request,'ultimage_trainer_launch_pack.html')

def advanced_lead_generation_package(request):
    return render(request,'advanced_lead_generation_package.html')