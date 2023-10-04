
#report for every student
def student_render_pdf_view(request,*args,**kwargs):
    id=kwargs.get('id')
    student=get_object_or_404(Student,UID=id)
    c=Class_attendance.objects.get(student=student)
    template_path = 'attendance_marker/pdf2.html'
    context = {'student': student,'c':c}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'  # Your SMTP server (e.g., smtp.gmail.com)
EMAIL_PORT = 587  # Port for SMTP (587 for TLS, 465 for SSL)
EMAIL_USE_TLS = True  # Use TLS (True or False)
EMAIL_USE_SSL = False  # Use SSL (True or False)
EMAIL_HOST_USER = 'your_email@example.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your_password'  # Your email password or app-specific password
DEFAULT_FROM_EMAIL = 'your_email@example.com'  # The email to be used as the 'from' address

# views.py or any appropriate file

from django.core.mail import send_mail

def send_email():
    subject = 'Hello, Django Email'
    message = 'This is a test email sent from Django.'
    from_email = 'your_email@example.com'
    recipient_list = ['recipient@example.com']  # List of recipient email addresses

    send_mail(subject, message, from_email, recipient_list)


# views.py

from django.shortcuts import render
from .utils import send_email  # Import the send_email function

def send_email_view(request):
    send_email()  # Call the send_email function
    return render(request, 'email_sent.html')


# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('send_email/', views.send_email_view, name='send_email'),
]
