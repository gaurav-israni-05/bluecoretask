from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task()
def send_email_sync(recipient_list, subject=None, body=None):
    """
    Task to send email to a recipient list
    :param recipient_list: 
    :param subject: 
    :param body: 
    :return: 
    """
    status = send_mail(subject=subject,
                       message=body,
                       from_email=settings.EMAIL_HOST_USER,
                       recipient_list=recipient_list)
    return status
