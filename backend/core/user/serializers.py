from rest_framework import serializers
from ..base.models import Sms, User


class UserSerializerCreate(serializers.ModelSerializer):
    """
    Serializer for creating a new user. with necessary inputs used in create view.
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # def create(self,password, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     user.set_password(password)
    #     return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance


class SmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sms
        fields = '__all__'
