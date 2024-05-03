
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if 'mob' in attrs:
            if not attrs['mob'].isdigit():
                raise serializers.ValidationError('Invalid mobile number')
            if (len(attrs['mob'])!=10):
             raise serializers.ValidationError('Mobile number should be of 10 digits')
        return super().validate(attrs)
    class Meta:
        model=User
        fields=['username','password','mob']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

