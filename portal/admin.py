from django.contrib import admin
from .models import LeaveRequest, Payroll, PerformanceReview

admin.site.register(LeaveRequest)
admin.site.register(Payroll)
admin.site.register(PerformanceReview)
