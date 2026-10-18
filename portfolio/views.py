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
          'title': 'News Aggregator API',
          'technologies': ['Python', 'FastAPI', 'Requests', 'REST API'],
          'description': 'REST API to fetch, search and normalize news from an external service, with parameter validation and a separate service layer.',
          'image_static': 'portfolio/assets/img/projects/news-aggregator-api.svg',
          'url': 'https://github.com/ale687/news-aggregator-api'
        },
        {
          'title': 'Football Data Dashboard',
          'technologies': ['Python', 'SQLite', 'FastAPI', 'ETL'],
          'description': 'ETL pipeline with Python, SQLite, FastAPI and a dashboard for football match analytics.',
          'image_static': 'portfolio/assets/img/projects/football_data_dashboard.png',
          'url': 'https://github.com/ale687/football_data_pipeline'  
        },
        {
        'title': 'PDF Data Extractor',
        'technologies': ['Python', 'PyMuPDF', 'Tabula'],
        'description': 'Python application that extracts structured data from PDF files using PyMuPDF and Tabula.',
        'image_static': 'portfolio/assets/img/projects/pdf_data_extractor.png',
        'url': 'https://github.com/ale687/pdf-data-extractor'
        },
        {
        'title': 'Weather App',
        'technologies': ['Python', 'Streamlit', 'OpenWeather API'],
        'description': 'Weather forecast dashboard built with Streamlit and the OpenWeather API.',
        'image_static': 'portfolio/assets/img/projects/Weather_App.png',
        'url': 'https://weather-forecast-data.streamlit.app/'
        },
        {
        'title': 'To-Do App',
        'technologies': ['Python', 'Streamlit'],
        'description': 'A simple Streamlit to-do app to add, manage, and track tasks.',
        'image_static': 'portfolio/assets/img/projects/To-do_App.png',
        'url': 'https://ale687-my-todo-app-web-1p4c95.streamlit.app/'
        }, 
    ]
    
    projects_to_show = list(db_projects)
    if projects_to_show:
        # Keep tags available for the existing projects managed through the admin.
        known_projects = {project['url']: project['technologies'] for project in fallback_projects}
        for project in projects_to_show:
            project.technologies = known_projects.get(project.url, [])
        if not any(project.url == fallback_projects[0]['url'] for project in projects_to_show):
            projects_to_show.insert(0, fallback_projects[0])
    else:
        projects_to_show = fallback_projects
    
    return render(request, 'portfolio/projects.html', {'projects': projects_to_show})

def certifications(request):
    return render(request, "portfolio/certifications.html")

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
