# Django Imports in alphabetical order
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response

# App imports in alphabetical order
from email_notifications.serializers import EmailModelSerializer
from email_notifications.tasks import send_email_sync


def response(data, code=status.HTTP_200_OK, error=""):
    """
    Overrides rest_framework response
    :param data: data to be send in response
    :param code: response status code(default has been set to 200)
    :param error: error message(if any, not compulsory)
    """
    return_dict = {"error": error, "response": data}
    return Response(data=return_dict, status=code)


def send_and_save_emails(recipient_list, async,  subject=None, body=None):
    """
    This function sends the email to the provided recipient
    :param recipient_list: 
    :param async: 
    :param subject: 
    :param body: 
    :return: 
    """
    email_object_list = []
    for recipient in recipient_list:
        email_object = {'from_email': settings.EMAIL_HOST_USER,
                        'to_email': recipient,
                        'subject': subject,
                        'body': body}
        email_object_list.append(email_object)
    # Saving all the emails in single db hit
    email_save_serializer = EmailModelSerializer(data=email_object_list, many=True)
    if not email_save_serializer.is_valid():
        # Return if any error in saving emails, with proper error message
        return {'status': False, 'error_message': repr(email_save_serializer.errors)}
    email_save_serializer.save()
    if not async:
        # Sending the mails synchronously, the function waits till all the emails are sent
        send_mail(subject=subject,
                  message=body,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=recipient_list)
    else:
        # Sending the mails asynchronously, the function moves on and the mails are sent in the background
        send_email_fn = send_email_sync.delay
        for recipient in recipient_list:
            send_email_fn(recipient_list=[recipient], subject=subject, body=body)
    return {'status': True, 'error_message': ""}


def make_email_filter_params(email, from_date=None, to_date=None):
    """
    Making dynamic filter parameters for the email query
    From Date and To Date are optional filters that can be sent
    :param email: 
    :param from_date: 
    :param to_date: 
    :return: 
    """
    email_filter_params = {'to_email': email, 'is_deleted': False}
    if to_date:
        # If to_date is sent, fetch emails before or equal to this date
        email_filter_params['created_at__lte'] = to_date
    if from_date:
        # If from_date is sent, fetch emails after or equal to this date
        email_filter_params['created_at__gte'] = from_date
    return email_filter_params


