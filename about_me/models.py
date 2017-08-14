from django.db import models

# Create your models here.


class Profile(models.Model):
    """
        This model holds data of a user's profile fetched from about.me's site.
        Fields fetched: username, full_name, bio, location, website.
        Refine Model make data searchable.
    """
    username = models.CharField(max_length=50, unique=True, blank=False)
    fullname = models.CharField(max_length=100, blank=False)
    website = models.URLField(max_length=200, blank=True)
    image = models.URLField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    bio = models.CharField(blank=False, max_length=200)

    class Meta:
        verbose_name = 'about.me Profile'
        verbose_name_plural = 'about.me Profiles'


class Interest(models.Model):
    interest = models.CharField(max_length=50, blank=False)
    profile = models.ManyToManyField(Profile)

    class Meta:
        verbose_name = 'about.me Interest'
        verbose_name_plural = 'about.me Interests'


class Role(models.Model):
    profile = models.ManyToManyField(Profile)
    role = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'about.me Role'
        verbose_name_plural = 'about.me Roles'


class SocialReach(models.Model):
    profile = models.ForeignKey(Profile)
    network = models.CharField(max_length=20, blank=False)
    link = models.URLField(max_length=200, blank=False)

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'


class MetaData(models.Model):
    field = models.CharField(max_length=50, blank=False)
    value = models.CharField(max_length=100, blank=False)
    profile = models.ForeignKey(Profile)

    class Meta:
        verbose_name = 'Meta Data'
        verbose_name_plural = 'Meta Data'
