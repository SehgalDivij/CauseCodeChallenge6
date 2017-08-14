from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=50)
    full_name = serializers.CharField(max_length=50)
    image = serializers.URLField()
    bio = serializers.CharField()
    website = serializers.URLField()
    location = serializers.CharField(max_length=80)
    interests = serializers.ListField(child=serializers.CharField())
    roles = serializers.ListField(child=serializers.CharField())
    social_reach = serializers.SerializerMethodField()
    meta_data = serializers.SerializerMethodField()

    def get_social_reach(self, obj):
        reach = {}
        for item in obj['social_reach']:
            for network, link in item.items():
                reach[network] = link
        return reach

    def get_meta_data(self, obj):
        meta = {}
        for item in obj['meta_data']:
            for field, value in item.items():
                meta[field] = value
        return meta
