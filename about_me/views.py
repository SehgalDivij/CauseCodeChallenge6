from .models import *
from .serializers import ProfileSerializer
from rest_framework import views
from rest_framework.response import Response
from .utils import save_about_me_profile
# Create your views here.


class Profiles(views.APIView):
    """
        Will fetch data for a public profile present at
        www://http:about.me/{user_name} and enter it into database.

        If already present, it will simply return the record for that username.

        If no user with the entered user name exists, a message is returned
        stating the same.

        To fetch data, make POST request to the URL: /api/about_me/profiles/
         with body as the following: {"username":"user_name here"}
    """
    queryset = Profile.objects.all()

    def make_profile_object(self, profile, interest, role, s_reach, meta):
        profile = {
            'user_name': profile.username,
            'full_name': profile.fullname,
            'website': profile.website,
            'image': profile.image,
            'bio': profile.bio,
            'location': profile.location,
            'interests': interest,
            'roles': role,
            'social_reach': s_reach,
            'meta_data': meta
        }
        return profile

    def get_related_records(self, record):
        interest = Interest.objects.filter(profile=record)
        role = Role.objects.filter(profile=record)
        social_reach = SocialReach.objects.filter(profile=record)
        meta_data = MetaData.objects.filter(profile=record)
        return (interest, role, social_reach, meta_data)

    def post(self, *args, **kwargs):
        try:
            username = self.request.data['username']
            user = Profile.objects.get(username=username)
            if user is not None:
                interest, role, social_reach, meta_data = self.get_related_records(user)
                profile = self.make_profile_object(user, interest, role, s_reach, meta)
                profiles_list = ProfileSerializer(profiles, many=True)
                return Response(data=profiles_list.data)
        except KeyError:
            return Response(data="Please enter username")
        record = save_about_me_profile(username)
        if isinstance(record, str):
            return Response(data=record)
        else:
            profile = self.make_profile_object(record.prof, record.interest, record.role, record.s_reach, record.meta)
            profiles_list = ProfileSerializer(profiles, many=True)
            return Response(data=profiles_list.data)

    def get(self, *args, **kwargs):
        records = Profile.objects.all()
        profiles = []
        if len(records) > 0:
            for record in records:
                interest, role, social_reach, meta_data = self.get_related_records(record)
                profile = self.make_profile_object(record, interest, role, social_reach, meta_data)
                profiles.append(profile)
        profiles_list = ProfileSerializer(profiles, many=True)
        print(profiles_list.data)
        return Response(data=profiles_list.data)
