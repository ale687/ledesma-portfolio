from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage


def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    db_projects = Project.objects.all()
    
    fallback_projects = [
        {
          'title': 'Football Data Dashboard',
          'description': 'ETL pipeline with Python, SQLite, FastAPI and a dashboard for football match analytics.',
          'image_static': 'portfolio/assets/img/projects/football_data_dashboard.png',
          'url': 'https://github.com/ale687/football_data_pipeline'  
        },
        {
        'title': 'PDF Data Extractor',
        'description': 'Python application that extracts structured data from PDF files using PyMuPDF and Tabula.',
        'image_static': 'portfolio/assets/img/projects/pdf_data_extractor.png',
        'url': 'https://github.com/ale687/pdf-data-extractor'
        },
        {
        'title': 'Weather App',
        'description': 'Weather forecast dashboard built with Streamlit and OpenWeather Api.',
        'image_static': 'portfolio/assets/img/projects/Weather_App.png',
        'url': 'https://weather-forecast-data.streamlit.app/'
        },
        {
        'title': 'To-Do App',
        'description': 'A simple Streamlit to-do app to add, manage, and track task.',
        'image_static': 'portfolio/assets/img/projects/To-do_App.png',
        'url': 'https://ale687-my-todo-app-web-1p4c95.streamlit.app/'
        }, 
    ]
    
    projects_to_show = db_projects if db_projects.exists() else fallback_projects
    
    return render(request, 'portfolio/projects.html', {'projects': projects_to_show})

def contact(request):
    if request.method == "GET":
        return render(request, "portfolio/contact.html")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        messages.error(request, "Please complete all fields.")
        return redirect("contact")

    email_message = EmailMessage(
        subject=f"Portfolio Contact — {name}",
        body=(
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_TO_EMAIL],
        reply_to=[email],
    )

    try:
        email_message.send(fail_silently=False)
        messages.success(request, "Message sent successfully!")
    except Exception as e:
        print("EMAIL EXCEPTION:", str(e))
        messages.error(request, "Could not send message right now.")

    return redirect("contact")