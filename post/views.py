import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from post.const import CONTENT_TYPE

from post.utils import BlogPostsRetrieve, BlogPostHandler


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class BlogPost(View):
    """
        BlogPost view handles the crud operations of the user posts -
            create,
            get,
            update,
            delete
    """

    def post(self, request):
        """
            Create all types of post by calling the BlogPostHandler class
            with post_create_handler method.
            Args:
                request (django.http.request.HttpRequest): HttpRequest object
            Returns:
                response (django.http.response.HttpResponse): HttpResponse object
        """
        try:
            request_body = json.loads(request.body)
            post = BlogPostHandler(request_body=request_body).post_create_handler()
            return HttpResponse(json.dumps(post), status=200, content_type=CONTENT_TYPE)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
            return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)

    def get(self, request, post_id):
        """
            Calls the post_get_handler method to get the post details by Id.
            Args:
                request (django.http.request.HttpRequest): HttpRequest object
                post_id (str): Post unique Id
            Returns:
                response (django.http.response.HttpResponse): HttpResponse object
        """
        try:
            post = BlogPostHandler().post_get_handler(post_id=post_id)
            return HttpResponse(json.dumps(post), status=200, content_type=CONTENT_TYPE)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
            return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)

    def patch(self, request, post_id):
        """
            Calls the post_update_handler method to update post details by Id.
            Args:
                request (django.http.request.HttpRequest): HttpRequest object
                post_id (str): Post unique Id
            Returns:
                response (django.http.response.HttpResponse): HttpResponse object
        """
        try:
            request_body = json.loads(request.body)
            post = BlogPostHandler(request_body).post_update_handler(post_id=post_id)
            return HttpResponse(json.dumps(post), status=200, content_type=CONTENT_TYPE)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
            return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)

    def delete(self, request, post_id):
        """
            Calls the post_delete_handler method to delete the post by Id.
            Args:
                request (django.http.request.HttpRequest): HttpRequest object
                post_id (str): Post unique Id
            Returns:
                response (django.http.response.HttpResponse): HttpResponse object
        """
        try:
            response = BlogPostHandler().post_delete_handler(post_id=post_id)
            return HttpResponse(json.dumps({'success': response}), status=200, content_type=CONTENT_TYPE)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
            return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)


@method_decorator(csrf_exempt, name="dispatch")
class FetchBlogPosts(View):
    """
        BlogTypes view handles GET method to return all the blog types.
    """
    def get(self, request):
        """
            Calls the blog posts method to fetch the blog types.
            Args:
                request (django.http.request.HttpRequest): HttpRequest object
            Returns:
                response (django.http.response.HttpResponse): HttpResponse object
        """
        try:
            blog_types = BlogPostsRetrieve().fetch_all_blog_posts()
            return HttpResponse(json.dumps(blog_types), status=200, content_type='application/json')
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
            return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)
