from django.urls import path
from . import views

urlpatterns = [
    path('', views.careers, name='careers'),
    path('frontend-developer/', views.frontend_detail, name='frontend-detail'),
    path('ml-engineer/', views.ml_detail, name='ml-detail'),
    path('apply/frontend/', lambda request: views.apply_for_job(request, 'Frontend Developer'), name='apply-frontend'),
path('apply/ml/', lambda request: views.apply_for_job(request, 'AI/ML Engineer'), name='apply-ml'),
path('application-success/', views.application_success, name='application-success'),

    path('apply/<str:job_title>/', views.apply_for_job, name='apply-job'),
    
]
