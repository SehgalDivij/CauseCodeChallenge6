from bs4 import BeautifulSoup
import requests
from html.parser import *


def is_user_profile(body):
    """
        If body has a class has-ledge, it is a user profile.
        else, it can be rejected.
    """
    if body.find('div', attrs={'class':'profile-column'}) is not None:
        return True
    else:
        return False


def get_user_profile_image(body):
    """
        Get user's profile image.
    """
    attrs = [attr.split(':', 1) for attr in body.find('div', 'head').find('div')['style'].split(';')]
    url_dirty = attrs[0][1]
    url_clean = url_dirty[4:-1]
    return url_clean


def get_user_name(body):
    """
        Get user's full name.
    """
    return body.find('div', 'profile-content').find('div', 'head').find('h1', 'name').get_text()


def get_roles_and_location(body):
    """
        Get user roles(list of roles) and current location.
        return: tuple that contains:
            1. list of roles
            2. location
    """
    roles = [role.get_text() for role in body.find('div', 'profile-content').find('div', 'head').find_all('span', 'role')]
    location = body.find('div', 'profile-content').find('div', 'head').find('span', 'location').find('span', 'location').get_text()
    return roles, location


def get_user_web_site(body):
    """
        Get user website's link and tag used for website.
        return: user's tag for link, link to web site.
    """
    return (body.find('div', 'body').find('section', 'spotlight').find('a').get_text(),
        body.find('div', 'body').find('section', 'spotlight').find('a')['href'])


def get_user_bio(body):
    """
        Get user's long bio.
    """
    bio = ''
    for p in body.find('div', 'body').find('section', 'bio').find_all('p'):
        bio = '%s\n' % p.get_text()
    return str(bio)


def get_user_interests(body):
    """
        Get user's interests - each interest is preceeded by a '#'.
        return: list of interests
    """
    return [p.get_text().lstrip('#') for p in body.find('div', 'body').find('section', 'interests').find_all('li', 'interest')]


def get_user_meta_info(body):
    """
        Get metadata about user such as work, jobs, schools etc.
    """
    meta_section = body.find('div', 'body').find('section', 'meta')
    meta_data = {}
    if meta_section is not None:
        print('meta_section: %s' % meta_section.get_text())
        meta_raw = meta_section.find_all('li', 'meta-section')
        print('meta raw: %s' %  meta_raw)
        if meta_raw is not None:
            for item in meta_raw:
                category = item.find('div', 'meta-header').get_text()
                data = [_item.get_text() for _item in item.find_all('li', 'meta-item')]
                meta_data[category] = data
    return meta_data


def get_user_social_links(body):
    """
        Get User Social Links in an array.
    """
    social_links = body.find('div', 'body').find_all('a', 'social-link')
    links = []
    for link in social_links:
        name = str(link['title'].split(' ')[-1])
        if not name.lower() in ['message', 'email']:
            url = str(link['href'])
            links.append({ name: url })
    return links


def get_page_layout(body):
    """
        Get layout type of page.
        Currently, not useful.
    """
    profile_classes = body.find('div', 'profile-column').find('div', 'profile-container').div['class']
    # return (('small' in profile_classes) : 'small' ? (('medium' in profile_classes) : 'medium' ? 'large'))
    return ('small' in profile_classes and 'small' or ('medium' in profile_classes and 'medium' or 'large'))


def get_profile_info(user_name: str):
    """
        Fetches a user profile from www.about.me/{user_name}
        If the page exists, i.e, the proper profile is returned,
            information is extracted from the page and shown to the user.
        If the page does not exist, the about.me homepage is shown and
            message is displayed saying that no such profile exists.
    """
    session = requests.session()
    res_page = session.get('http://www.about.me/%s' % user_name).text.replace("\n", "").strip()
    body = BeautifulSoup(res_page, 'html.parser').find('body')
    if is_user_profile(body):
        roles, location = get_roles_and_location(body)
        website_tag, link = get_user_web_site(body)
        profile = {
            'full_name': get_user_name(body),
            'bio': get_user_bio(body),
            'interests': get_user_interests(body),
            'meta_data': get_user_meta_info(body),
            'social_reach': get_user_social_links(body),
            'roles': roles,
            'location': location,
            'website': link,
            'website_tag': website_tag,
            'image': get_user_profile_image(body)
        }
        return profile
    else:
        return 'No profile found for that username'
