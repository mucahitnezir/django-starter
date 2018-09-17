import os

import sendgrid
from sendgrid.helpers.mail import Personalization, Mail, Email
from setting.models import Setting


class MailHelper:

    def __init__(self, api_key=os.environ.get('SENDGRID_API_KEY')):
        print("Started")
        self.sg = sendgrid.SendGridAPIClient(apikey=api_key)

    def send(self, body):
        try:
            self.sg.client.mail.send.post(request_body=body)
            return True
        except Exception as error:
            return False

    def send_contact_form_mail(self, message):
        parameters = Setting.get_multiple(['contact_form_notification_mail', 'company_name'])
        p = Personalization()
        p.add_to(Email(parameters['contact_form_notification_mail'], parameters['company_name']))
        p.dynamic_template_data = {
            'fullName': message.full_name,
            'emailAddress': message.email_address,
            'phoneNumber': message.phone_number,
            'message': message.message,
            'subject': message.subject
        }

        mail = Mail()
        mail.from_email = Email('contact-form@mucahitnezir.com', message.full_name)
        mail.template_id = 'd-ed945c87123d4e44828fbfbb4f29e1a8'
        mail.reply_to = Email(message.email_address, message.full_name)
        mail.add_personalization(p)

        return self.send(mail.get())
