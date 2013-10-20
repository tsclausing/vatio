from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

from .models import PendingUserInvite


def user_invite_notification(user_invite_uuid):
    pui = PendingUserInvite.objects.get(uuid=user_invite_uuid)
    email_body = """
COOKIES
    """ % {
        'email': pui.email,
        'link': 'https://' + settings.SITE + reverse('user_invite', args=[user_invite_uuid]),
    }

    email = EmailMessage(
        subject='You\'ve been invited to use vat.io',
        body=email_body,
        to=[pui.email]
    )
    email.send(fail_silently=False)
