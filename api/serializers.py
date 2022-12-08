from rest_framework.serializers import ModelSerializer

from api.models import Mailing, Client, Message


class MailingSerializer(ModelSerializer):
    class Meta:
        model = Mailing
        fields = (
            'id',
            'date_mailing',
            'text',
            'client_filter',
            'date_stop',
        )


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'tel',
            'code',
            'tag',
            'timezone',
        )


class MessageSerializer(ModelSerializer):
    
    class Meta:
        model = Message
        fields = (
            'id',
            'date',
            'status',
            'id_mailing',
            'id_client',
        )