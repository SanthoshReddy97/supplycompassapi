from django.forms import model_to_dict

from post.models import Text, Image, Video, Github, Bookmark, Quote, Post
from post import const
from django.core import serializers


def create_blogs_post(post):
    """
        Create a blog post
    """
    if post.blog_type == 'text':
        post = Text(body=post.body,
                    title=post.title,
                    tags=post.tags,
                    blog_type='text')
    elif post.blog_type == 'image':
        post = Image(image_url=post.image_url,
                     title=post.title,
                     tags=post.tags,
                     blog_type='image')
    elif post.blog_type == 'video':
        post = Video(video_url=post.video_url,
                     title=post.title,
                     tags=post.tags,
                     blog_type='video')
    if post.blog_type == 'github':
        post = Github(github_embeded_url=post.github_embeded_url,
                      title=post.title,
                      tags=post.tags,
                      blog_type='github')
    elif post.blog_type == 'quote':
        post = Quote(quote_text=post.quote_text,
                     source=post.source,
                     title=post.title,
                     tags=post.tags,
                     blog_type='quote')
    elif post.blog_type == 'bookmark':
        post = Bookmark(bookmark_url=post.bookmark_url,
                        title=post.title,
                        tags=post.tags,
                        blog_type='bookmark')
    post.save()
    return model_to_dict(post)


def get_blog_post(post):
    """
        GET blog posts
    """
    post = const.DB_MODELS.get(post.blog_type).objects.get(post_ptr_id=post.post_id)
    return model_to_dict(post)


def update_blog_post(post):
    """
        Update blog post
    """
    post_data = const.DB_MODELS.get(post.blog_type).objects.get(post_ptr_id=post.post_id)
    for key, value in post.update_items.items():
        setattr(post_data, key, value)
    post_data.save()
    return model_to_dict(post_data)


def delete_blog_post(post):
    """
        Delete blog post
    """
    post = Post.objects.get(id=post.post_id)
    post.delete()
    return True


def get_all_posts():
    """
        Get all the posts
    """
    response = []
    posts = Post.objects.all()
    for post in posts:
        post_type = post.blog_type
        post_data = getattr(post, post_type)
        response.append(model_to_dict(post_data))
    return response
