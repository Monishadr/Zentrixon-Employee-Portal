from django.shortcuts import render

def careers(request):
    return render(request, 'jobs/careers.html')

def frontend_detail(request):
    return render(request, 'jobs/frontend_detail.html')

def ml_detail(request):
    return render(request, 'jobs/ml_detail.html')

from django.shortcuts import render, redirect
from .forms import JobApplicationForm

def apply_frontend(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Here you can handle saving, emailing, etc.
            return redirect('careers')  # Redirect after success
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_form.html', {
        'form': form,
        'job_title': 'Frontend Developer'
    })

def apply_ml(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('careers')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_form.html', {
        'form': form,
        'job_title': 'AI/ML Engineer'
    })
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import JobApplicationForm
from .models import Application

def apply_for_job(request, job_title):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_title = job_title
            application.save()

            # Send email notification
            send_mail(
                subject=f"New Application for {job_title}",
                message=f"Applicant: {application.name}\nEmail: {application.email}\nPhone: {application.phone}",
                from_email='drmonisha833@gmail.com',
                recipient_list=['monishadr27@gmail.com'],
            )

            return redirect('application-success')
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_form.html', {'form': form, 'job_title': job_title})



def application_success(request):
    return render(request, 'jobs/success.html')

def apply_frontend(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_title = 'Frontend Developer'
            application.save()
            return redirect('application-success')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_form.html', {'form': form, 'job_title': 'Frontend Developer'})


def apply_ml(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_title = 'AI/ML Engineer'
            application.save()
            return redirect('application-success')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_form.html', {'form': form, 'job_title': 'AI/ML Engineer'})

from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import Application
from django.conf import settings

def apply_for_job(request, job_title):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES.get('resume')
            application = form.save(commit=False)
            application.job_title = job_title
            application.save()

            # ✅ Email to Admin with resume attachment
            admin_email = EmailMessage(
                subject=f"New Application for {job_title}",
                body=f"""
A new job application was submitted.

Name: {application.name}
Email: {application.email}
Phone: {application.phone}
Job Title: {job_title}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['drmonisha833@gmail.com'],  # Admin email
            )

            if resume_file:
                admin_email.attach(resume_file.name, resume_file.read(), resume_file.content_type)

            admin_email.send()

            # ✅ Email confirmation to applicant
            send_mail(
                subject='Thank you for applying at Zentrixon!',
                message=f"""
Hi {application.name},

Thank you for applying for the role of {job_title} at Zentrixon Technologies.

Our team will review your application and get back to you soon.

Regards,  
Zentrixon HR Team
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[application.email],
            )

            return redirect('application-success')
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_form.html', {'form': form, 'job_title': job_title})
