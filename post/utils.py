from post.interface import IBlogPostsRetrieveAbstract, IBlogPostHandlerAbstract
from post.models import Post
from post.common import create_blogs_post, get_blog_post, update_blog_post, delete_blog_post, get_all_posts


class BlogPostHandler(IBlogPostHandlerAbstract):
    """
        BlogPostHandler takes care of CRUD operations of the post.
    """

    def __init__(self, request_body=None, blog_post=None):
        """
            Initialise the settings for CRUD operations

            Args:
                request_body (dict): Request body received in the API
                blog_post : Blog post common method for DB operations.
            Returns:
                post : Return the post details.

        """
        if request_body is None:
            request_body = dict()
        self.title = request_body.get('title')
        self.tags = request_body.get('tags')
        self.blog_type = request_body.get('blog_type')
        self.body = request_body.get('body')
        self.blog_post = blog_post
        self.image_url = request_body.get('image_url')
        self.video_url = request_body.get('video_url')
        self.quote_text = request_body.get('quote_text')
        self.source = request_body.get('source')
        self.bookmark_url = request_body.get('bookmark_url')
        self.github_embeded_url = request_body.get('github_embeded_url')
        self.update_items = request_body.get('update_items')
        self.post_id = ''

    def post_create_handler(self):
        """
            Create Post handler
        """
        self.blog_post = create_blogs_post
        return self.__global_post_handler()

    def __global_post_handler(self):
        """
            Global post handler which calls common blog post method for DB operations.
        """
        return self.blog_post(self)

    def post_get_handler(self, post_id):
        """
            Get Post details handler
        """
        post_data = Post.objects.get(id=post_id)
        self.blog_type, self.post_id = post_data.blog_type, post_data.id
        self.blog_post = get_blog_post
        return self.__global_post_handler()

    def post_update_handler(self, post_id):
        """
            Update Post handler
        """
        post_data = Post.objects.get(id=post_id)
        self.blog_type, self.post_id = post_data.blog_type, post_data.id
        self.blog_post = update_blog_post
        return self.__global_post_handler()

    def post_delete_handler(self, post_id):
        """
            Delete post handler
        """
        self.post_id = post_id
        self.blog_post = delete_blog_post
        return self.__global_post_handler()


class BlogPostsRetrieve(IBlogPostsRetrieveAbstract):
    """
        Query the DB and fetches all the blog posts
    """

    def __init__(self):
        pass

    def fetch_all_blog_posts(self):
        """
            Returns the blog types
        """
        return get_all_posts()

