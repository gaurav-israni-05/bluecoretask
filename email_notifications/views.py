# Django Imports in alphabetical order
from rest_framework.views import APIView

# App imports in alphabetical order
from bluecore_email_systems.exceptions import GenericException
from email_notifications import utils as email_utils
from email_notifications.models import Email
from email_notifications.serializers import *


class EmailView(APIView):
    def post(self, request):
        email_request_serializer = EmailRequestSerializer(data=request.data)
        if not email_request_serializer.is_valid():
            raise GenericException(detail=email_request_serializer.errors)
        email_dict = email_utils.send_and_save_emails(**email_request_serializer.validated_data)
        if not email_dict.get('status'):
            raise GenericException(detail=email_dict.get('error_message'))
        return email_utils.response("Emails saved successfully")

    def get(self, request):
        email_fetch_serializer = EmailFetchSerializer(data=request.query_params)
        if not email_fetch_serializer.is_valid():
            raise GenericException(detail=email_fetch_serializer.errors)
        email_filter_params = email_utils.make_email_filter_params(**email_fetch_serializer.validated_data)
        email_objects = Email.objects.filter(**email_filter_params)
        email_serializer_data = EmailModelSerializer(email_objects, many=True).data
        return email_utils.response({'email_data': email_serializer_data})

