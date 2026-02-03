import os
import requests
from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages


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
    if request.method == "GET":
        return render(request, "portfolio/contact.html")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    api_key = os.getenv("SENDGRID_API_KEY")
    to_email = os.getenv("CONTACT_TO_EMAIL")
    from_email = os.getenv("SENDGRID_FROM_EMAIL", to_email) 

    if not api_key or not to_email or not from_email:
        messages.error(request, "Email service not configured.")
        return redirect("contact")

    if not name or not email or not message:
        messages.error(request, "Please complete all fields.")
        return redirect("contact")

    payload = {
        "personalizations": [{"to": [{"email": to_email}]}],
        "from": {"email": from_email},
        "reply_to": {"email": email},
        "subject": f"Portfolio Contact — {name}",
        "content": [
            {
                "type": "text/plain",
                "value": f"Name: {name}\nEmail: {email}\n\n{message}",
            }
        ],
    }

    try:
        r = requests.post(
            "https://api.sendgrid.com/v3/mail/send",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=10,
        )

        print("SENDGRID STATUS:", r.status_code)
        print("SENDGRID RESPONSE:", r.text)

        if 200 <= r.status_code < 300:
            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "SendGrid rejected the request.")
    except Exception as e:
        print("SENDGRID EXCEPTION:", str(e))
        messages.error(request, "Could not send message right now.")

    return redirect("contact")


  
