from .scraper import get_profile_info
from .models import *
from django.db import transaction


def add_to_database(username, user_data):
    interests = []
    roles = []
    s_reaches = []
    metas = []
    with transaction.atomic():
        prof = Profile(
            username=username,
            fullname=user_data['full_name'],
            location=user_data['location'],
            website=user_data['website'],
            image=user_data['image'],
            bio=user_data['bio'])
        prof.save()
        for interest in user_data['interests']:
            interest = Interest(interest = interest)
            interest.save()
            interest.profile.add(prof)
            interest.save()
            interests.append(interest)
        for role in user_data['roles']:
            role = Role(role = role)
            role.save()
            role.profile.add(prof)
            role.save()
            roles.append(role)
        for network, link in user_data['social_reach'].items():
            s_reach = SocialReach(profile=prof, link = link,network = network)
            s_reach.save()
            s_reaches.append(s_reach)
        for field, value in user_data['meta_data'].items():
            meta = MetaData(profile=prof,field = field,value = value)
            meta.save()
            metas.append(meta)
        return (prof, interests, roles, s_reaches, metas)


def save_about_me_profile(username: str):
    user_data = get_profile_info(username)
    if isinstance(user_data, str):
        return user_data
    else:
        return add_to_database(username, user_data)
