from app.DAO.comments import Comments
from app.DAO.common_data import CommonData


class CommentsDAO(CommonData):

    def __init__(self, path):
        super().__init__(path)

    def _load_comments(self):
        comments_data = self._load_data()

        list_of_comments = [Comments(**comment_data) for comment_data in comments_data]

        return list_of_comments

    def get_comments_all(self):
        comments = self._load_comments()
        return comments

    def get_comments_by_post_id(self, post_id):
        if type(post_id) != int:
            raise TypeError("post_id должен быть число!")
        comments = self._load_comments()
        matching_comments = [comment for comment in comments if comment.post_id == post_id]
        return matching_comments


