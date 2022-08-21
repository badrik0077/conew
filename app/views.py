from flask import Blueprint, render_template, abort, request

from app.DAO.post_dao import PostDAO
from app.DAO.comments_dao import CommentsDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS, DATA_PATH_BOOKMARKS


post_blueprint = Blueprint('blueprint_post', __name__, template_folder='templates')
posts_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)


@post_blueprint.get('/')
def all_posts_page():
    all_posts = posts_dao.get_all()
    query = request.args.get("s", "")
    if query == "":
        posts_search = []
    else:
        posts_search = posts_dao.search_in_content(query)
    return render_template('index.html',
                           posts=all_posts,
                           posts_search=posts_search,
                           query=query,
                           len_posts=len(posts_search))


@post_blueprint.get('/post/<int:pk>')
def one_posts_page(pk):
    one_post = posts_dao.get_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(post_id=pk)
    if one_post is None:
        abort(404, 'Такого поста не существует')
    return render_template('post.html', post=one_post, comments=comments, len_comments=len(comments))


@post_blueprint.get('/user/<user_name>')
def page_by_user_name(user_name):
    posts = posts_dao.get_by_poster(user_name)
    if not posts:
        abort(404, 'Такого пользователя не существует')
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@post_blueprint.get('/search/')
def page_search():
    query = request.args.get("s", "")
    if query == "":
        posts = []
    else:
        posts = posts_dao.search_in_content(query)
    return render_template('search.html', posts=posts, query=query, len_posts=len(posts))
