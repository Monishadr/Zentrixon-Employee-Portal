from django.db import models

class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    link = models.URLField(blank=True)
    team = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend Developers'),
        ('backend', 'Backend Developers'),
        ('qa', 'Quality Analysts')
    ])

    def __str__(self):
        return self.name

# models.py
from django.db import models

class Ourteams(models.Model):
    TEAM_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('QA', 'QA'),
    ]

    image = models.ImageField(null=True, blank=True, default='default.jpg')
    name = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    team_name = models.CharField(max_length=100, choices=TEAM_CHOICES, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.team_name})"

class Ourwork(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    description = models.TextField(null=True, blank=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    Source_code = models.CharField(max_length=200, null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Ourteams(models.Model):
    TEAM_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('QA', 'QA'),
    ]

    image = models.ImageField(upload_to='team_images/', null=True, blank=True, default='default.jpg')
    name = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    team_name = models.CharField(max_length=100, choices=TEAM_CHOICES, null=True)
    link = models.URLField(null=True, blank=True)  # LinkedIn or GitHub

    def __str__(self):
        return f"{self.name} ({self.team_name})"
