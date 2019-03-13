from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView

from home.forms import ContactForm
from setting.models import Setting


class HomeView(TemplateView):
    template_name = 'homepage.html'
    extra_context = {'title': _('Homepage')}


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'contact/index.html'
    success_url = reverse_lazy('contact')
    success_message = _('Message created successfully!')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        params = ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url', 'phone', 'email', 'gmap_code')
        data['params'] = Setting.get_multiple(params)
        data['title'] = _('Contact')
        return data

    def form_valid(self, form):
        message = form.save(commit=False)
        # Prepare mail parameters
        receiver = Setting.get_one('contact_form_notification_mail')
        html_message = render_to_string('mail_templates/contact-form.html', {'message': message})
        plain_message = strip_tags(html_message)
        # Send email
        email = EmailMultiAlternatives(message.subject, plain_message, settings.DEFAULT_FROM_EMAIL, [receiver],
                                       reply_to=[message.email_address])
        email.attach_alternative(html_message, "text/html")
        if email.send(fail_silently=True):
            message.save()
            return super().form_valid(form)
        else:
            messages.warning(self.request, _('Email did not send!'))
            return redirect('contact')

    def form_invalid(self, form):
        messages.warning(self.request, _('Message did not created!'))
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs['initial'] = {
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email_address': self.request.user.email,
            }
        return kwargs
