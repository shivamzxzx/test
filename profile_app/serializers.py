
from rest_framework import  serializers

from profile_app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['pincode']  # Only include the pincode field

    def update(self, instance, validated_data):
        # Update only the pincode
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.save()
        return instance
