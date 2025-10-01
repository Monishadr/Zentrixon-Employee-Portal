from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def team(request):
    return render(request, 'core/team.html')
from django.shortcuts import render
from .models import OurTeam  # Assuming your model is named OurTeam

def team_frontend(request):
    ourteams = OurTeam.objects.filter(role__icontains='frontend')
    return render(request, 'core/team_detail.html', {'ourteams': ourteams})

def team_backend(request):
    ourteams = OurTeam.objects.filter(role__icontains='backend')
    return render(request, 'core/team_detail.html', {'ourteams': ourteams})

def team_qa(request):
    ourteams = OurTeam.objects.filter(role__icontains='quality')
    return render(request, 'core/team_detail.html', {'ourteams': ourteams})
from .models import TeamMember

def frontend_team(request):
    members = TeamMember.objects.filter(team='frontend')
    return render(request, 'core/team_detail.html', {
        'ourteams': members,
        'team_type': 'Frontend Developers'
    })

def backend_team(request):
    members = TeamMember.objects.filter(team='backend')
    return render(request, 'core/team_detail.html', {
        'ourteams': members,
        'team_type': 'Back-end Developers'
    })

def qa_team(request):
    members = TeamMember.objects.filter(team='qa')
    return render(request, 'core/team_detail.html', {
        'ourteams': members,
        'team_type': 'Quality Analysts'
    })

# Example for frontend developers
def frontend_team(request):
    ourteams = [
        {'name': 'Priya Sharma', 'role': 'React Developer', 'image': 'images/team1.jpg'},
        {'name': 'Rohit Mehta', 'role': 'Angular Developer', 'image': 'images/team2.jpg'},
        {'name': 'Ananya Gupta', 'role': 'UI Designer', 'image': 'images/team3.jpg'},
    ]
    return render(request, 'core/team_detail.html', {'ourteams': ourteams, 'team_type': 'Frontend'})

def backend_team(request):
    ourteams = [
        {'name': 'Akash Reddy', 'role': 'Django Developer', 'image': 'images/backend1.jpg'},
        {'name': 'Sneha Rao', 'role': 'API Specialist', 'image': 'images/backend2.jpg'},
    ]
    return render(request, 'core/team_detail.html', {'ourteams': ourteams, 'team_type': 'Backend'})

from django.shortcuts import render
from .models import Ourteams, Ourwork

def team_category_view(request, team_name):
    members = Ourteams.objects.filter(team_name__iexact=team_name)
    return render(request, 'knowmore/team_detail.html', {
        'ourteams': members,
        'team_type': team_name
    })

def ourwork(request):
    ourwork = Ourwork.objects.all()
    return render(request, 'knowmore/ourwork.html', {'ourwork': ourwork})
def team_category_view(request, team_name):
    members = Ourteams.objects.filter(team_name__iexact=team_name)
    return render(request, 'core/team_detail.html', {
        'ourteams': members,
        'team_type': team_name
    })
