from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('team/frontend/', views.team_frontend, name='team-frontend'),
    path('team/backend/', views.team_backend, name='team-backend'),
    path('team/qa/', views.team_qa, name='team-qa'),
    path('ourwork/', views.ourwork, name='ourwork'),
    path('teams/<str:team_name>/', views.team_category_view, name='team-category'),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
