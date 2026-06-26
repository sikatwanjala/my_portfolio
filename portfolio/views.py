# views.py
from django.shortcuts import get_object_or_404, render
from django.http import FileResponse
from .models import Document
# from .forms import ContactForm


def index(request):
    # Fetch all documents to display on the page
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})

def download_document(request, doc_id):
    # Retrieve the specific document uploaded by the admin
    document = get_object_or_404(Document, id=doc_id)
    
    # Open the file in binary read mode
    file_handle = document.file.open('rb')

    # Send file response with correct content-type for docx
    response = FileResponse(file_handle, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    
    # Force download dialog and specify filename
    response['Content-Disposition'] = f'attachment; filename="{document.file.name.split("/")[-1]}"'
    return response



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.core.mail import send_mail

# from .forms import ContactForm


# def contact_view(request):

#     if request.method == "POST":

#         form = ContactForm(request.POST)

#         if form.is_valid():

#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             full_message = f"""
#                 Name: {name}
#                 Email: {email} 
#                 Message:{message} """

#             send_mail(
#                 subject,
#                 full_message,
#                 email,
#                 ['your_email@gmail.com'],
#                 fail_silently=False,
#             )

#             messages.success(
#                 request,
#                 "Message sent successfully!"
#             )

#             return redirect('contact')

#     else:
#         form = ContactForm()

#     return render(
#         request,
#         'contact.html',
#         {
#             'form': form
#         }
#     )



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

# from .forms import ContactForm


# def index(request):

#     form = ContactForm()

#     if request.method == "POST":

#         form = ContactForm(request.POST)

#         if form.is_valid():

#             contact = form.save()

#             # Admin email
#             admin_html = render_to_string(
#                 'emails/contact_email.html',
#                 {
#                     'name': contact.name,
#                     'email': contact.email,
#                     'phone': contact.phone,
#                     'subject': contact.subject,
#                     'message': contact.message,
#                 }
#             )

#             email = EmailMultiAlternatives(
#                 subject=f"New Website Message - {contact.subject}",
#                 body=contact.message,
#                 from_email="yourgmail@gmail.com",
#                 to=["yourinbox@gmail.com"]
#             )

#             email.attach_alternative(admin_html, "text/html")
#             email.send()

#             # Auto Reply
#             reply_html = render_to_string(
#                 'emails/auto_reply.html',
#                 {
#                     'name': contact.name,
#                     'message': contact.message
#                 }
#             )

#             reply = EmailMultiAlternatives(
#                 subject="Thank You For Contacting Us",
#                 body="We received your message.",
#                 from_email="yourgmail@gmail.com",
#                 to=[contact.email]
#             )

#             reply.attach_alternative(reply_html, "text/html")
#             reply.send()

#             messages.success(
#                 request,
#                 "Your message has been sent successfully."
#             )

#             return redirect('index')

#     return render(
#         request,
#         'index.html',
#         {
#             'form': form
#         }
#     )




from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import ContactMessage


def contact_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not all([name, email, phone, subject, message]):
            messages.error(request, "Please fill in all required fields.")
            return redirect("contact")

        # Save to database
        contact = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        try:

            # Admin Email
            admin_html = render_to_string(
                "emails/contact_email.html",
                {
                    "name": contact.name,
                    "email": contact.email,
                    "phone": contact.phone,
                    "subject": contact.subject,
                    "message": contact.message,
                }
            )

            admin_email = EmailMultiAlternatives(
                subject=f"New Website Message: {contact.subject}",
                body=contact.message,
                from_email="yourgmail@gmail.com",
                to=["yourinbox@gmail.com"],
            )

            admin_email.attach_alternative(
                admin_html,
                "text/html"
            )

            admin_email.send()

            # Auto Reply
            reply_html = render_to_string(
                "emails/auto_reply.html",
                {
                    "name": contact.name,
                    "message": contact.message,
                }
            )

            auto_reply = EmailMultiAlternatives(
                subject="Thank You For Contacting Us",
                body="We have received your message.",
                from_email="yourgmail@gmail.com",
                to=[contact.email],
            )

            auto_reply.attach_alternative( reply_html, "text/html")

            auto_reply.send()
            messages.success(request, "Your message has been sent successfully.")

        except Exception as e: messages.error( request, f"Email error: {str(e)}")

        return redirect("contact")

    return render(request, "index.html")




from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import ContactMessage


def contact_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        if not all([
            name,
            email,
            phone,
            subject,
            message_text
        ]):
            messages.error(
                request,
                "Please fill all required fields."
            )
            return redirect("contact")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message_text
        )

        # Send email
        try:

            send_mail(
                subject=f"Website Contact: {subject}",
                message=f"""
                    Name: {name}

                    Email: {email}

                    Phone: {phone}

                    Message: {message_text}
                """,
                from_email=name,
                recipient_list=[
                    "sikatafilex@gmail.com"
                ],
                fail_silently=False
            )

            messages.success(
                request,
                "Message sent successfully."
            )

        except Exception as e:

            messages.error(
                request,
                f"Error sending email: {e}"
            )

        return redirect("contact")

    return render(
        request,
        "index.html"
    )