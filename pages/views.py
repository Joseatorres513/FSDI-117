from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Rest of your settings file...

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ExperiencePageView(TemplateView):
    template_name = "pages/experience.html"

# def contact_view(request):
    # form = ContactForm()
    # return render(request, "pages/contact.html", {"form": form})

def contact_view(request):
    if request.method == "POST":
        # validate and send email
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Valid data")

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            message_body  = "This is an email from your portfolio/nName:{name}/nEmail:{email}/nMessage:{message}"
            send_mail(
                "Email from Portfolio",
                message,
                email,
                ['tocachu@gmail.com'] # <- who should receive the email?

            )
        else:
            print("Invalid from data")


    else:
        # display the page
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})














def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=full_message,
            from_email='your_email@example.com',
            recipient_list=['your_email@example.com'],
        )

        messages.success(request, "Thanks for reaching out! I’ll get back to you soon.")
        return redirect('home')

    return redirect('home')

def testing_view(request):
    return render(request, "pages/test.html")
