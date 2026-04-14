from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def about_me_view(request):
    return render(request, 'pages/mission.html')


def experience_view(request):
    return render(request, 'pages/skills.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()

            email_context = {
                'name':         msg.name,
                'email':        msg.email,
                'inquiry_type': msg.get_inquiry_type_display(),
                'subject':      msg.subject,
                'budget':       msg.get_budget_display() if msg.budget else '',
                'timeline':     msg.get_timeline_display() if msg.timeline else '',
                'message':      msg.message,
                'heard_from':   msg.get_heard_from_display() if msg.heard_from else '',
            }

            plain_text = (
                f"New inquiry from {msg.name} ({msg.email})\n\n"
                f"Type:     {email_context['inquiry_type']}\n"
                f"Subject:  {msg.subject}\n"
                f"Budget:   {email_context['budget'] or 'Not specified'}\n"
                f"Timeline: {email_context['timeline'] or 'Not specified'}\n"
                f"Heard:    {email_context['heard_from'] or 'Not specified'}\n\n"
                f"Message:\n{msg.message}"
            )

            html_body = render_to_string('emails/contact_notification.html', email_context)

            try:
                email = EmailMultiAlternatives(
                    subject=f'[Portfolio] {email_context["inquiry_type"]} — {msg.name}',
                    body=plain_text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[msg.email],
                )
                email.attach_alternative(html_body, 'text/html')
                email.send(fail_silently=False)
            except Exception:
                pass  

            return render(request, 'pages/contact.html', {'success': True})

        return render(request, 'pages/contact.html', {'form': form, 'error': True})

    form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
