from django.core.mail import send_mail as django_send_mail
from django.template.loader import render_to_string

from access.models import users
from access import user_object
import random
import string


def send_mail_register(receiver, name):
    subject = 'Activate Connectify Account'
    length = random.randint(5, 10)
    secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    user_object.secret_code = secret_code
    html_string = render_to_string('access\email_register_file.html',
                                   {
                                       'name': name,
                                       'secret_code': secret_code,
                                   })

    try:
        django_send_mail(subject, '', from_email='nircas.official@gmail.com',
                         recipient_list=[receiver],
                         html_message=html_string)
    except Exception as e:
        print(e)
        return False

    return True
