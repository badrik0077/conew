import logging

from flask import Blueprint, jsonify

from app.DAO.comments_dao import CommentsDAO
from app.DAO.post_dao import PostDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

posts_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)

api_blueprint = Blueprint('api_blueprint', __name__)
api_logger = logging.getLogger('api_logger')


@api_blueprint.get('/posts/')
def api_all_posts():
    all_posts = posts_dao.get_all()
    api_logger.debug(f'Запрошены все посты')
    return jsonify([post.post_dict() for post in all_posts]), 200


@api_blueprint.get('/posts/<int:pk>')
def api_single_posts(pk):
    one_post = posts_dao.get_by_pk(pk)
    api_logger.debug(f'Запрошен пост {pk}')
    return jsonify(one_post.post_dict()), 200
