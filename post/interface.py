from abc import ABC, abstractmethod


class IBlogPostHandlerAbstract(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def post_create_handler(self):
        pass

    @abstractmethod
    def post_get_handler(self, post_id):
        pass

    @abstractmethod
    def post_update_handler(self, post_id):
        pass

    @abstractmethod
    def post_delete_handler(self, post_id):
        pass


class IBlogPostsRetrieveAbstract(ABC):

    @abstractmethod
    def __init__(self):
        self.blog_types = list()

    @abstractmethod
    def fetch_all_blog_posts(self):
        pass
