from rest_framework import serializers


class InterestSerializer(serializers.Serializer):
    interest = serializers.CharField(max_length=50, read_only=True)


class RoleSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=50, read_only=True)


class SocialReachSerializer(serializers.Serializer):
    network = serializers.CharField(max_length=20, read_only=True)
    link = serializers.URLField(max_length=200, read_only=True)


class MetaDataSerializer(serializers.Serializer):
    field = serializers.CharField(max_length=20, read_only=True)
    value = serializers.CharField(max_length=20, read_only=True)


class ProfileSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=50)
    full_name = serializers.CharField(max_length=50)
    image = serializers.URLField()
    bio = serializers.CharField()
    interests = InterestSerializer(many=True)
    roles = RoleSerializer(many=True)
    social_reach = SocialReachSerializer(many=True)
    website = serializers.URLField()
    meta_data = MetaDataSerializer(many=True)
    location = serializers.CharField(max_length=80)
