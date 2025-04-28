from django.shortcuts import render
from django.views.generic import TemplateView
from .models import HomePage

# Create your views here.
class Home(TemplateView):
    def get(self,request):
        homepage = HomePage.objects.first()
        title = "Home"
        return render(request,'home.html',{"title":title,"homepage":homepage})

def about_us(request):
    title = "About Us"
    return render(request,'about_us.html',{"title":title})

def contact_us(request):
    title = "Contact Us"
    return render(request,'contact_us.html',{"title":title})

def beginner_to_pro(request):
    title = "Beginner to Pro pack"
    return render(request,'beginner_to_pro.html',{"title":title})

def fast_track_training(request):
    title = "Fast Track Training Pack"
    return render(request,'fast_track_training.html',{"title":title})

def workshops(request):
    title = "Workshops"
    return render(request,'workshops.html',{"title":title})

def live_session(request):
    title = "Live Session"
    return render(request,'live_session.html',{"title":title})

def skill_to_trainer(request):
    title = "Skill To Trainer Pack"
    return render(request,'skill_to_trainer.html',{"title":title})

def ultimage_trainer_launch_pack(request):
    title = "Ultimate Trainer Launch Pack"
    return render(request,'ultimage_trainer_launch_pack.html',{"title":title})

def advanced_lead_generation_package(request):
    title = "Advanced Lead Generation Pack"
    return render(request,'advanced_lead_generation_package.html',{"title":title})