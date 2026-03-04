from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "name",
            "price",
            "billing",
            "start_date",
            "next_payment_date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "next_payment_date",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        sub = Subscription(**validated_data)
        sub.next_payment_date = sub.start_date
        sub.calculate_next_payment()
        sub.save()
        return sub