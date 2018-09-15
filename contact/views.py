from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

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
                messages.success(request, _('Message created successfully!'))
            else:
                messages.error(request, _('Email did not send!'))
        else:
            messages.error(request, _('Message did not created!'))
        return redirect('contact:index')
    else:
        # Get form
        initial_form_data = {}
        if request.user.is_authenticated:
            initial_form_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email_address': request.user.email,
            }
        form = ContactForm(initial=initial_form_data)
        # Get contact parameters
        params = ['facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url', 'phone_number', 'email_address', 'gmap_iframe_code']
        parameters = Setting.get_multiple(params)
        # Page context
        context = {
            'title': _('Contact'),
            'form': form,
            'params': parameters
        }
        # Render page
        return render(request, 'contact/index.html', context)
