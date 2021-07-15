from post.models import Text, Image, Video, Github, Bookmark, Quote

DB_MODELS = {
    'text': Text,
    'image': Image,
    'video': Video,
    'github': Github,
    'quote': Quote,
    'bookmark': Bookmark
}
CONTENT_TYPE = 'application/json'
