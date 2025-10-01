from django.contrib import admin

# Register your models here.
from .models import TeamMember

admin.site.register(TeamMember)
from django.contrib import admin
from .models import Ourteams, Ourwork

admin.site.register(Ourteams)
admin.site.register(Ourwork)
