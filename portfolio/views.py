from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render



def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    db_projects = Project.objects.all()
    
    fallback_projects = [
        {
        'title': 'To-Do App',
        'description': 'A simple Streamlit to-do app to add, manage, and track task.',
        'image_static': 'portfolio/assets/img/projects/To-do_App.png',
        'url': 'https://ale687-my-todo-app-web-1p4c95.streamlit.app/'
        },
        {
            'title': 'Weather App',
            'description': 'Weather forecast dashboard built with Streamlit and OpenWeather Api.',
            'image_static': 'portfolio/assets/img/projects/Weather_App.png',
            'url': 'https://weather-forecast-data.streamlit.app/'
        },
    ]
    
    projects_to_show = db_projects if db_projects.exists() else fallback_projects
    
    return render(request, 'portfolio/projects.html', {'projects': projects_to_show})
    
def contact(request):
    succes = False
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        full_message = f"""
    
        New contact message from portfolio:
        
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """

        send_mail(
            subject="New Portfolio Contact Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        
        succes = True
    
    return render(request, 'portfolio/contact.html', {'success': succes})