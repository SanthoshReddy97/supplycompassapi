from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Post(models.Model):
    """
        Post model to store all the common post info
    """
    BLOG_TYPES = (
        ('TEXT', 'text'),
        ('IMAGE', 'image'),
        ('VIDEO', 'video'),
        ('GITHUB', 'github'),
        ('QUOTE', 'quote'),
        ('BOOKMARK', 'bookmark')
    )
    title = models.CharField(max_length=300, null=True, blank=True)
    tags = ArrayField(
        models.CharField(max_length=50, null=True, blank=True),
        size=8,
    )
    blog_type = models.CharField(max_length=20, choices=BLOG_TYPES)

    def __str__(self):
        s = ''
        for k, v in self.__dict__.items():
            s += ('%s: %s\n' % (k, v))
        return s


class Text(Post):
    """
        Text blog post
    """
    body = models.CharField(max_length=1048, null=True, blank=True)


class Image(Post):
    """
        Image blog post
    """
    image_url = models.URLField(null=True, blank=True)


class Video(Post):
    """
        Video blog post
    """
    video_url = models.URLField(null=True, blank=True)


class Github(Post):
    """
        Github blog post
    """
    github_embeded_url = models.URLField(null=True, blank=True)


class Quote(Post):
    """
        Quote blog post
    """
    quote_text = models.CharField(max_length=4096, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)


class Bookmark(Post):
    """
        Bookmark blog post
    """
    bookmark_url = models.URLField(null=True, blank=True)
