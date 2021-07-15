from django.conf.urls import url
from post.views import FetchBlogPosts, BlogPost

post_url_patterns = [
    url(r'^data/?$', FetchBlogPosts.as_view()),
    url(r'^$', BlogPost.as_view()),
    url(r'^(?P<post_id>.+)/?$', BlogPost.as_view()),
]
