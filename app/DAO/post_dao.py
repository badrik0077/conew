from app.DAO.common_data import CommonData
from app.DAO.post import Post


class PostDAO(CommonData):

    def __init__(self, path):
        super().__init__(path)

    def _load_posts(self):
        posts_data = self._load_data()

        list_of_post = [Post(**post_data) for post_data in posts_data]

        return list_of_post

    def get_all(self):
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        if type(pk) != int:
            raise TypeError("pk должен быть число!")
        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        if type(substring) != str:
            raise TypeError("substring должно  быть строкой!")
        substring = substring.lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts

    def get_by_poster(self, user_name):
        if type(user_name) != str:
            raise TypeError("user_name должно  быть строкой!")
        user_name = user_name.lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]
        return matching_posts
