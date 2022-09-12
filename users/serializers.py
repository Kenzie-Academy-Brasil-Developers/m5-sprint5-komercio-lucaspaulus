from rest_framework import serializers
from .models import Users

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'is_seller', 'date_joined', 'is_active', 'is_superuser']
        read_only_fields = ['date_joined','is_superuser','is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user