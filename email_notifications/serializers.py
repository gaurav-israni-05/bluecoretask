# Direct imports
import datetime

# Django imports
from rest_framework import serializers

# App imports
from email_notifications.models import *


class EmailRequestSerializer(serializers.Serializer):
    """
    This serializer is used to validate the request parameters for send bulk email
    """
    recipient_list = serializers.ListField(child=serializers.EmailField())
    subject = serializers.CharField(max_length=256)
    body = serializers.CharField()
    async = serializers.BooleanField(default=False)


class EmailFetchSerializer(serializers.Serializer):
    """
    This serializer validates the request parameters for fetching emails of a particular user
    """
    email = serializers.EmailField()
    from_date = serializers.DateField(required=False)
    to_date = serializers.DateField(required=False)

    def validate(self, data):
        now = datetime.date.today()
        # Checking if from_date is newer than current_date
        if data.get('from_date') and data.get('from_date') > now:
            raise serializers.ValidationError('From Date cannot has to be within current date')
        # Checking if to_date is newer than current_date
        if data.get('to_date') and data.get('to_date') > now:
            raise serializers.ValidationError('To Date cannot has to be within current date')
        # Checking if from_date is newer than to_date
        if data.get('from_date') and data.get('to_date'):
            if data.get('from_date') > data.get('to_date'):
                raise serializers.ValidationError('From Date cannot be greater than To Date')
        return data


class EmailModelSerializer(serializers.ModelSerializer):
    """
    Model serializer to save and serializer data
    """
    class Meta:
        model = Email
        fields = '__all__'

