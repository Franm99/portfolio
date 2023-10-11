from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .models import Project, Skill
from .forms import ContactForm

def home(request):
    """ Portfolio main page """
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by('-mastery')
    return render(request, 'home.html', context={"projects": projects, "skills": skills})


def landing_page(request):
    return redirect(reverse("portfolio:home"))


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', context={"projects": projects})


# def contact(request):
#     # If this is a POST request, the form data needs to be processed.
#     if request.method == "GET":
#         form = ContactForm()    
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data["subject"]
#             from_email = form.cleaned_data["email"]
#             message = form.cleaned_data["message"]
            
#             try:
#                 send_mail(subject, message, from_email, ["fran.moreno.se@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect(reverse("portfolio:home"))
#     return render(request, "contact.html", {"form": form}) 

def contact(request):
    host_mail = "fran.moreno.se@gmail.com"
    return render(request, 'contact.html', context={"host_mail": host_mail})

def thanks(request):
    return render(request, 'thanks.html')
        
    
