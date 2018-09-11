from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm
from helpers.mail import MailHelper
from setting.models import Setting


def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get message
            message = form.save(commit=False)
            # Create mail helper instance and send mail
            mail_helper = MailHelper()
            send = mail_helper.send_contact_form_mail(message)
            if send:
                message.save()
                messages.success(request, 'Message created successfully!')
            else:
                messages.error(request, 'Email did not send.')
        else:
            messages.error(request, 'Message did not created!')
        return redirect('contact:index')
    else:
        # Get form
        form = ContactForm()
        # Get contact parameters
        params = ['facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url', 'phone_number', 'email_address', 'gmap_iframe_code']
        parameters = Setting.get_multiple(params)
        # Page context
        context = {
            'title': 'İletişim',
            'form': form,
            'parameters': parameters
        }
        # Render page
        return render(request, 'contact/index.html', context)