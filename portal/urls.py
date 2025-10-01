from django.urls import path
from .views import (
    PortalLoginView,
    portal_dashboard,
    leave_detail,
    payroll_detail,
    reviews_detail,
    generate_payslip_pdf,cancel_leave,
    download_payslip_excel, # ✅ Add this line
)

urlpatterns = [
    path('', PortalLoginView.as_view(), name='portal-login'),
    path('dashboard/', portal_dashboard, name='portal-dashboard'),
    path('leave/', leave_detail, name='leave-detail'),
    path('payroll/', payroll_detail, name='payroll-detail'),
    path('reviews/', reviews_detail, name='reviews-detail'),
    path('payroll/payslip/<str:month>/', generate_payslip_pdf, name='download-payslip'), path('leave/', leave_detail, name='leave-detail'),
    path('leave/cancel/<int:leave_id>/', cancel_leave, name='cancel-leave'),  # <- ADD THIS # ✅ This will now work
    path('payroll/payslip/<str:month>/excel/', download_payslip_excel, name='download-payslip-excel'),  # ✅ Add this
    path('payroll/payslip/<str:month>/pdf/', generate_payslip_pdf, name='download-payslip'),
path('payroll/payslip/<str:month>/excel/', download_payslip_excel, name='download-payslip-excel'),
path('portal/payroll/payslip/<str:month>/', generate_payslip_pdf, name='download-payslip'),
path('portal/payroll/payslip-excel/<str:month>/', download_payslip_excel, name='download-payslip-excel'),

]
